import pandas as pd

df1 = pd.read_csv('csv file1')
df2 = pd.read_csv('csv file2')

df1.columns.values[0] = 'Country'
df2.columns.values[0] = 'Country'


df1['Country'] = df1['Country'].str.strip()
df2['Country'] = df2['Country'].str.strip()

matched_df = pd.merge(df1, df2, on='Country', how='inner')

all_df = pd.merge(df1, df2, on='Country', how='outer', indicator=True)
unmatched_df = all_df[all_df['_merge'] != 'both'].drop(columns=['_merge'])

matched_df.to_csv('kmatched_cleaned.csv', index=False)
unmatched_df.to_csv('kunmatched_cleaned.csv', index=False)

print("Done: Cleaned and merged.")
