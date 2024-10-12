from sqlalchemy import create_engine
import pandas as pd

# Define your server and database
server = 'DESKTOP-FCEDQJG'  # e.g., 'localhost' or '192.168.1.100'
database = 'cancer'  # e.g., 'mydb'

# Create connection string using ODBC Driver 17
connection_string = (
  f'mssql+pyodbc://{server}/{database}'
  '?driver=ODBC Driver 17 for SQL Server;'
  'Trusted_Connection=yes'  # Remove this line if using SQL Server Authentication
)

# Create the SQLAlchemy engine
engine = create_engine(connection_string)

# Test the connection
try:
    with engine.connect() as connection:
        print("Connection successful!")
        # Example: Fetch data from a table
        df = pd.read_sql("SELECT TOP 10 * FROM your_table_name", connection)
        print(df)
except Exception as e:
    print(f"Error: {e}")
