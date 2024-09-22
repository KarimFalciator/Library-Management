import sqlite3
import random

# Function to generate a unique random 5-digit ID
def generate_unique_id():
    return random.randint(10000, 99999)

# Function to connect to the SQLite database
def connect_to_db(db_name='customer_database.db'):
    return sqlite3.connect(db_name)

# Function to create the customer table
def create_customer_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customer (
        id INTEGER PRIMARY KEY,
        password TEXT NOT NULL,
        first_name TEXT NOT NULL,
        surname TEXT NOT NULL,
        email TEXT NOT NULL,
        address TEXT NOT NULL
    )
    ''')
    conn.commit()

# Function to insert a customer into the database
def new_customer(conn, password, first_name, surname, email, address):
    cursor = conn.cursor()
    customer_data = (generate_unique_id(), password, first_name, surname, email, address)
    
    cursor.execute('''
    INSERT INTO customer (id, password, first_name, surname, email, address)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', customer_data)
    conn.commit()

# Function to close the database connection
def close_connection(conn):
    conn.close()

# Main function to run the program
def main():
    # Connect to the database
    conn = connect_to_db()

    # Create the customer table
    create_customer_table(conn)

    # Insert a customer (Example data)
    new_customer(conn, 'password123', 'John', 'Doe', 'john.doe@email.com', '123 Main St')

    # Close the connection
    close_connection(conn)
    print("Customer table created and data inserted!")

# Run the program
if __name__ == "__main__":
    main()
