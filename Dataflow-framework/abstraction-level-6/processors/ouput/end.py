# processors/output/end.py
class EndProcessor:
    def process(self, lines):
        for line in lines:
            print(f"Processed: {line}")
