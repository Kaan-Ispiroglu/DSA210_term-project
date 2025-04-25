import pandas as pd

# Load the CSV file
df = pd.read_csv('csv file')

# List of column positions to remove (0-based indexing)
column_indexes_to_remove = []  # e.g., remove 1st, 3rd, and 5th columns

# Get the column names at those positions
column_names_to_remove = [df.columns[i] for i in column_indexes_to_remove]

# Drop the columns
df = df.drop(columns=column_names_to_remove)

# Save to a new CSV
df.to_csv('ccleaned_file.csv', index=False)

print(f"✅ Columns removed: {column_names_to_remove}")
