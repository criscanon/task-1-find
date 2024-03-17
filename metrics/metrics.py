# metrics/metrics.py

import time
import inspect

def measure_time_in_milliseconds(algorithm, *args, num_runs=10, **kwargs):
    total_execution_time = 0

    for _ in range(num_runs):
        start_time = time.time() * 1000000
        result = algorithm(*args, **kwargs)
        end_time = time.time() * 1000000
        total_execution_time += (end_time - start_time)

    average_execution_time = total_execution_time / num_runs
    return result, average_execution_time

def count_basic_operations(algorithm, *args, **kwargs):
    result = algorithm(*args, **kwargs)
    source_code = inspect.getsource(algorithm)
    basic_operations = source_code.count('<') + source_code.count('>')
    return result, basic_operations

def count_function_calls(algorithm, *args, **kwargs):
    result = algorithm(*args, **kwargs)
    source_code = inspect.getsource(algorithm)
    function_calls = source_code.count('(')
    return result, function_calls
