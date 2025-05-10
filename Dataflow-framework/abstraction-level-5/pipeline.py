import yaml
import importlib

class DAGPipeline:
    def __init__(self, dag, routes):
        self.dag = dag  # dict: node_name -> (processor_instance, input_names)
        self.routes = routes  # dict: (node_name, tag) -> [next_node_names]

    def run(self, input_stream):
        # Initial input
        cache = {"__root__": input_stream}

        # Initialize outputs for all nodes
        outputs = {name: [] for name in self.dag}
        for node_name, (processor, input_names) in self.dag.items():
            # Merge inputs
            merged_input = self.merge_inputs([cache.get(name, []) for name in input_names])
            # Run processor
            for tag, line in processor(merged_input):
                # Get next nodes using tag, fallback to 'info' if tag is None or not in routes
                next_nodes = self.routes.get((node_name, tag), [])
                if not next_nodes and tag is None:
                    next_nodes = self.routes.get((node_name, "info"), [])

                for next_node in next_nodes:
                    outputs[next_node].append((tag, line))

            cache[node_name] = outputs[node_name]

        # Drain the output from the last node (optional step for completeness)
        last_node = self.find_last_node()
        for _ in cache[last_node]:
            pass  # Drain output

    def merge_inputs(self, streams):
        for stream in streams:
            for item in stream:
                yield item

    def find_last_node(self):
        # Naively assume last added node is the output
        return list(self.dag.keys())[-1]

    @classmethod
    def from_yaml(cls, filepath):
        with open(filepath, "r") as f:
            config = yaml.safe_load(f)

        dag = {}
        for name, node in config["nodes"].items():
            module_path, class_name = node["factory"].rsplit(".", 1)
            module = importlib.import_module(module_path)
            cls_obj = getattr(module, class_name)
            processor = cls_obj()
            dag[name] = (processor, node.get("inputs", []))

        # Prepare tag-based routes
        routes = {}
        for route in config.get("routes", []):
            key = (route["from"], route["tag"])
            routes.setdefault(key, []).append(route["to"])

        return cls(dag, routes)
