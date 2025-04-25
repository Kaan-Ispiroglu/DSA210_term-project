import pandas as pd

df = pd.read_csv('csv file')

column_indexes_to_remove = [] 

column_names_to_remove = [df.columns[i] for i in column_indexes_to_remove]

df = df.drop(columns=column_names_to_remove)

df.to_csv('ccleaned_file.csv', index=False)

print(f"Columns removed: {column_names_to_remove}")
