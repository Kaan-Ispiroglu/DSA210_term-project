import pandas as pd

# Load the two datasets
df1 = pd.read_csv('csv file1')
df2 = pd.read_csv('csv file2')

# Standardize the first column to 'Country'
df1.columns.values[0] = 'Country'
df2.columns.values[0] = 'Country'

# ✅ Normalize 'Country' column: strip spaces and unify capitalization
df1['Country'] = df1['Country'].str.strip()
df2['Country'] = df2['Country'].str.strip()

# Optional: Also lowercase for strict consistency (remove if not desired)
# df1['Country'] = df1['Country'].str.lower()
# df2['Country'] = df2['Country'].str.lower()

# Merge based on cleaned country names
matched_df = pd.merge(df1, df2, on='Country', how='inner')

# Identify unmatched entries
all_df = pd.merge(df1, df2, on='Country', how='outer', indicator=True)
unmatched_df = all_df[all_df['_merge'] != 'both'].drop(columns=['_merge'])

# Save the cleaned results
matched_df.to_csv('kmatched_cleaned.csv', index=False)
unmatched_df.to_csv('kunmatched_cleaned.csv', index=False)

print("✅ Done: Cleaned and merged.")
