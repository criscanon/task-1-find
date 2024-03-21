from algorithms.linear_search import linear_search
from algorithms.kmp_search import kmp_search
from algorithms.boyer_moore_search import boyer_moore_search
from metrics.metrics import measure_time
from data_generator.data_generator import generate_data
from graphs.graph import create_graph
import pandas as pd

def run_experiment(algorithm, text, pattern, num_runs=10):
    result, avg_exec_time = measure_time(algorithm, text, pattern, num_runs=num_runs)
    return result, avg_exec_time

def main():
    experiment = [1125, 2250, 4500, 9000, 18000, 27000, 36000, 45000, 54000, 108000]
    results = []
    patterns = ["EEEEEEEEEE", "ABCABCABCD", "ABCDEFGHIJ", "ABCABCABCA"]
    
    for pattern in patterns:
        for text_length in experiment:
            text = generate_data(text_length=text_length)
            iteration = []
            iteration.append(len(text))
            iteration.append(len(pattern))

            # Linear Search
            result, avg_exec_time = run_experiment(linear_search, text, pattern)
            iteration.append(result)
            iteration.append(avg_exec_time)

            # KMP Search
            result, avg_exec_time = run_experiment(kmp_search, text, pattern)
            iteration.append(result)
            iteration.append(avg_exec_time)
            
            # Boyer-Moore Search
            result, avg_exec_time = run_experiment(boyer_moore_search, text, pattern)
            iteration.append(result)
            iteration.append(avg_exec_time)
            
            results.append(iteration)

    print(pd.DataFrame(results))
    create_graph(results=results, graphs=len(patterns), patterns=patterns)
    
    
if __name__ == "__main__":
    main()