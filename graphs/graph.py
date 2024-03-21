import matplotlib.pyplot as plt
import pandas as pd

def create_graph(results, graphs, patterns):
    # Calculate number of rows and columns for the subplot grid
    num_rows = (graphs + 1) // 2  # Asegura que se tenga al menos 1 fila
    num_cols = 2 if graphs > 1 else 1  # Si hay más de una gráfica, se usarán dos columnas
    
    # Calculate number of rows per graph
    rows_per_graph = len(results) // graphs
    
    # Create a list to store dataframes for each graph
    dfs = []
    
    # Split results into dataframes for each graph
    for i in range(graphs):
        start_idx = i * rows_per_graph
        end_idx = start_idx + rows_per_graph if i < graphs - 1 else None
        dfs.append(pd.DataFrame(results[start_idx:end_idx]))

    # Plotting
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(12, 8))
    fig.tight_layout(pad=3.0)  # Agrega espacio entre las gráficas

    for i, ax in enumerate(axes.flat):
        if i < graphs:
            df = dfs[i]
            ax.plot(df[0], df[3], label='linear_search')
            ax.plot(df[0], df[5], label='kmp_search')
            ax.plot(df[0], df[7], label='boyer_moore_search')
            ax.set_title(patterns[i])
            ax.set_xlabel("Text Length")
            ax.set_ylabel("Average Execution Time (us)")
            ax.legend()
            ax.grid(True)
        else:
            ax.axis('off')  # Desactiva los ejes para las gráficas faltantes

    plt.show()