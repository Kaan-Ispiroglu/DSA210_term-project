import pandas as pd

# Load the two CSV files
df1 = pd.read_csv('csv file', index_col=0)  # assumes first column is index
df2 = pd.read_csv('csv file', index_col=0)

# Concatenate the two DataFrames
merged_df = pd.concat([df1, df2])

# Sort by the index alphabetically
sorted_df = merged_df.sort_index()

# Save the sorted DataFrame to a new CSV
sorted_df.to_csv('merged_sorted_by_index.csv')

print("Merged and sorted by index CSV saved as 'merged_sorted_by_index.csv'.")
