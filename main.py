
import matplotlib.pyplot as plt
import time
import pandas as pd
from algorithms.linear_search import linear_search
from algorithms.kmp_search import kmp_search
from algorithms.boyer_moore_search import boyer_moore_search
from metrics.metrics import measure_time_in_milliseconds, count_basic_operations, count_function_calls
from data_generator.data_generator import generate_data

def run_experiment(algorithm, text, pattern, num_runs=10):
    result, avg_exec_time = measure_time_in_milliseconds(algorithm, text, pattern, num_runs=num_runs)
    _, basic_ops = count_basic_operations(algorithm, text, pattern)
    _, func_calls = count_function_calls(algorithm, text, pattern)
    return {
        "Algorithm": algorithm.__name__,
        "Text Length": len(text),
        "Pattern Length": len(pattern),
        "Average Execution Time (ms)": avg_exec_time,
        "Basic Operations": basic_ops,
        "Function Calls": func_calls
    }

def main():
    results = []

    for text_length in [5000, 10000, 15000, 20000, 50000]:
        for pattern_length in [2,3,4]:
            text, pattern = generate_data(text_length=text_length, pattern_length=pattern_length)

            # Linear Search
            results.append(run_experiment(linear_search, text, pattern))

            # KMP Search
            results.append(run_experiment(kmp_search, text, pattern))

            # Boyer-Moore Search
            results.append(run_experiment(boyer_moore_search, text, pattern))

    
    # Create a DataFrame from the results
    df = pd.DataFrame(results)

    # Print the DataFrame
    print(df)

    
    # Plotting
    plt.figure(figsize=(10, 6))

    for algo_name, algo_df in df.groupby("Algorithm"):
        plt.plot(algo_df["Text Length"], algo_df["Average Execution Time (ms)"], label=algo_name)

    plt.title("Algorithm Comparison")
    plt.xlabel("Text Length")
    plt.ylabel("Average Execution Time (ms)")
    plt.legend()
    plt.grid(True)

    # Show the plot and wait for user input
    plt.show()
    time.sleep(10)  # Espera 10 segundos antes de cerrar la ventana
    

if __name__ == "__main__":
    main()





"""
from algorithms.linear_search import linear_search
from algorithms.kmp_search import kmp_search
from algorithms.boyer_moore_search import boyer_moore_search
from metrics.metrics import measure_time_in_milliseconds, count_basic_operations, count_function_calls
from data_generator.data_generator import generate_data

def main():
    # Generate random data
    text, pattern = generate_data(text_length=1000000, pattern_length=4)

    # Linear Search
    result, avg_exec_time = measure_time_in_milliseconds(linear_search, text, pattern, num_runs=10)
    _, basic_ops_linear = count_basic_operations(linear_search, text, pattern)
    _, func_calls_linear = count_function_calls(linear_search, text, pattern)
    print("Linear Search Results:")
    print(f"  - Average Execution Time: {avg_exec_time} milliseconds")
    print(f"  - Basic Operations: {basic_ops_linear}")
    print(f"  - Function Calls: {func_calls_linear}")
    print(f"  - Result: {result}")

    # KMP Search
    result, avg_exec_time = measure_time_in_milliseconds(kmp_search, text, pattern, num_runs=10)
    _, basic_ops_kmp = count_basic_operations(kmp_search, text, pattern)
    _, func_calls_kmp = count_function_calls(kmp_search, text, pattern)
    print("\nKMP Search Results:")
    print(f"  - Average Execution Time: {avg_exec_time} milliseconds")
    print(f"  - Basic Operations: {basic_ops_kmp}")
    print(f"  - Function Calls: {func_calls_kmp}")
    print(f"  - Result: {result}")

    # Boyer-Moore Search
    result, avg_exec_time = measure_time_in_milliseconds(boyer_moore_search, text, pattern, num_runs=10)
    _, basic_ops_bm = count_basic_operations(boyer_moore_search, text, pattern)
    _, func_calls_bm = count_function_calls(boyer_moore_search, text, pattern)
    print("\nBoyer-Moore Search Results:")
    print(f"  - Average Execution Time: {avg_exec_time} milliseconds")
    print(f"  - Basic Operations: {basic_ops_bm}")
    print(f"  - Function Calls: {func_calls_bm}")
    print(f"  - Result: {result}")



if __name__ == "__main__":
    main()

"""