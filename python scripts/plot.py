import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("csv file")


def plot_against_all(df, col_x):

    if col_x not in df.columns:
        print(f"Column '{col_x}' not found in the DataFrame.")
        return

    for col_y in df.columns:
        if col_y != col_x:
            plt.figure(figsize=(10, 8))
            plt.scatter(df[col_x], df[col_y], marker='o', linestyle='-')
            plt.xlabel(col_x)
            plt.ylabel(col_y)
            plt.title(f"{col_x} vs {col_y}")
            plt.grid(True)
            plt.show()

plot_against_all(df, 'Quality of Life Value')

