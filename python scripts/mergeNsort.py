import pandas as pd

df1 = pd.read_csv('csv file', index_col=0)  # assumes first column is index
df2 = pd.read_csv('csv file', index_col=0)

merged_df = pd.concat([df1, df2])

sorted_df = merged_df.sort_index()

sorted_df.to_csv('merged_sorted_by_index.csv')

print("Merged and sorted by index CSV saved as 'merged_sorted_by_index.csv'.")
