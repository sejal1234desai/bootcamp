# processors/formatters/general.py
class GeneralProcessor:
    def process(self, lines):
        # Implement general processing logic
        for line in lines:
            yield "general", line  # Tag it as 'general'
