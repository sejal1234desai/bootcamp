# processors/format.py

class Format:
    def __init__(self, format_str="{tag}: {line}"):
        self.format_str = format_str

    def __call__(self, inputs):
        for tag, line in inputs:
            formatted_line = self.format_str.format(tag=tag, line=line)
            yield tag, formatted_line
