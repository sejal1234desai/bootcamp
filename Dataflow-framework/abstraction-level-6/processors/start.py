# processors/start.py
class StartProcessor:
    def process(self, lines):
        for line in lines:
            if 'error' in line:
                yield 'error', line
            elif 'warn' in line:
                yield 'warn', line
            else:
                yield 'general', line