# processors/filters/error.py
class ErrorProcessor:
    def process(self, lines):
        # Implement the logic for processing error lines
        for line in lines:
            if "error" in line.lower():
                yield "error", line  # Tag it as 'error'
