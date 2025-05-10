# processors/filters/warn.py
class WarnProcessor:
    def process(self, lines):
        # Implement the logic for processing warning lines
        for line in lines:
            if "warn" in line.lower():
                yield "warn", line  # Tag it as 'warn'
