#6
# Operation: Create a dictionary with counters, timers, etc., updated during execution

import time

metrics = {
    "requests_handled": 0,
    "processing_time": 0.0
}

def process_request():
    start_time = time.time()
    # Simulate request processing
    time.sleep(1)
    metrics["requests_handled"] += 1
    metrics["processing_time"] += (time.time() - start_time)

# Example usage:
process_request()
print(metrics)

# Output:
# {'requests_handled': 1, 'processing_time': 1.0002}
