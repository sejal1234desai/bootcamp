# 07_custom_serialize_graph.py

import pickle

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_node(self, node):
        self.nodes.add(node)
        if node not in self.edges:
            self.edges[node] = []

    def add_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            self.edges[node1].append(node2)
            self.edges[node2].append(node1)

    def __getstate__(self):
        # Custom serialization: Only serialize nodes and edges
        return {
            'nodes': list(self.nodes),
            'edges': self.edges
        }

    def __setstate__(self, state):
        # Custom deserialization: Rebuild the graph from nodes and edges
        self.nodes = set(state['nodes'])
        self.edges = state['edges']

    def __str__(self):
        return f"Nodes: {self.nodes}\nEdges: {self.edges}"

# Create a Graph instance
graph = Graph()
graph.add_node('A')
graph.add_node('B')
graph.add_edge('A', 'B')
graph.add_node('C')
graph.add_edge('A', 'C')

# Serialize the Graph object
with open("graph_data.pkl", "wb") as f:
    pickle.dump(graph, f)

print("Graph object serialized successfully.")
