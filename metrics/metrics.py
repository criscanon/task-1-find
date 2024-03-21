import time
import inspect

def measure_time(algorithm, *args, num_runs, **kwargs):
    total_execution_time = 0

    for _ in range(num_runs):
        start_time = time.perf_counter()
        result = algorithm(*args, **kwargs)
        end_time = time.perf_counter()
        total_execution_time += (end_time - start_time)

    average_execution_time = total_execution_time * 1e6/ num_runs
    return result, average_execution_time