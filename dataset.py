import sqlite3
import pandas as pd
import CONFIGURE
import os

# Path to the SQLite database
db_path = os.path.join(CONFIGURE.DATASET_PATH, "database.sqlite")

# Connect to the database
conn = sqlite3.connect(db_path)

# List all tables in the database
query = "SELECT name FROM sqlite_master WHERE type='table';"
tables = pd.read_sql(query, conn)
#print("Tables in the database:", tables)


####

# Load data from a table (replace 'Player' with the desired table name)
table_name = "Player"  # Example: Analyze Player table
df = pd.read_sql(f"SELECT * FROM {table_name}", conn)

# Display the first rows and column names
print(f"Columns in {table_name} table: {df.columns}")
print(df.head())
