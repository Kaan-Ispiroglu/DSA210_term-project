import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('csv file')

def plot_avg_quality_by_subregion(df, qol_column='Quality of Life Value', region_column='sub-region'):
    df_clean = df[[region_column, qol_column]].dropna()

    avg_qol = df_clean.groupby(region_column)[qol_column].mean().sort_values(ascending=False)

    plt.figure(figsize=(12, 6))
    avg_qol.plot(kind='bar')
    plt.ylabel('Average Quality of Life')
    plt.xlabel('sub-region')
    plt.title('Average Quality of Life by Subregion')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.grid(axis='y')
    plt.show()

plot_avg_quality_by_subregion(df)
