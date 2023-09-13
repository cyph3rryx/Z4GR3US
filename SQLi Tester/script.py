import sqlite3

# Function to connect to the SQLite database
def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect('data.db')  # You can also supply the special name ":memory:" to create a database in RAM
        print(f'successful connection with sqlite version {sqlite3.version}')
    except sqlite3.Error as error:
        print("Failed to connect", error)
    return conn

# Function to execute a query
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except sqlite3.Error as error:
        print(f"Failed to execute query: {error}")

# Function to select all rows from a table
def select_all_from_table(connection, table_name):
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM {table_name};')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Function to insert a new row into a table
def insert_into_table(connection, table_name, data):
    cursor = connection.cursor()
    placeholders = ', '.join('?' * len(data))
    cursor.execute(f"INSERT INTO {table_name} VALUES ({placeholders})", data)
    connection.commit()

# Function to update data in a table
def update_table(connection, table_name, column_to_update, new_value, condition_column, condition_value):
    cursor = connection.cursor()
    cursor.execute(f"UPDATE {table_name} SET {column_to_update} = ? WHERE {condition_column} = ?", (new_value, condition_value))
    connection.commit()

# Function to delete data from a table
def delete_from_table(connection, table_name, condition_column, condition_value):
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM {table_name} WHERE {condition_column} = ?", (condition_value,))
    connection.commit()

# Function to list all tables in the database
def list_all_tables(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(cursor.fetchall())

# Function to perform bulk insert
def bulk_insert_into_table(connection, table_name, data):
    cursor = connection.cursor()
    placeholders = ', '.join('?' * len(data[0]))
    cursor.executemany(f"INSERT INTO {table_name} VALUES ({placeholders})", data)
    connection.commit()

# Connect to the database
connection = create_connection()

# Create a table
create_table_query = """
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT,
    position TEXT,
    hireDate TEXT
);
"""
execute_query(connection, create_table_query)

# Insert data into the table
insert_into_table(connection, 'employees', (1, 'John', 'HR', 'Manager', '2017-01-04'))

# Select all data from the table
select_all_from_table(connection, 'employees')

# Update data in the table
update_table(connection, 'employees', 'name', 'Jane', 'id', 1)

# Delete data from the table
delete_from_table(connection, 'employees', 'id', 1)

# List all tables in the database
list_all_tables(connection)

# Bulk insert into the table
bulk_insert_into_table(connection, 'employees', [(2, 'Andrew', 'IT', 'Tech', '2018-02-06'), (3, 'Lea', 'Finance', 'Accountant', '2019-03-22')])

# Close the connection
connection.close()
