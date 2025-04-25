import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('csv file')

def plot_qol_on_map(df, lat_col='latitude', lon_col='longitude', qol_col='Quality of Life Value'):
    # Drop missing data
    df_clean = df[[lat_col, lon_col, qol_col]].dropna()

    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(
        df_clean[lon_col], 
        df_clean[lat_col], 
        c=df_clean[qol_col], 
        cmap='viridis', 
        s=80, 
        edgecolor='black', 
        alpha=0.8
    )

    plt.colorbar(scatter, label='Quality of Life')
    plt.xlabel('longitude')
    plt.ylabel('latitude')
    plt.title('Quality of Life by Location')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Example usage:
# df = pd.read_csv('your_data.csv')
plot_qol_on_map(df)
