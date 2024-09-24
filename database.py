import sqlite3
import random


# Function to connect to the SQLite database
def connect_to_db(db_name='log_info.db'):
    return sqlite3.connect(db_name)

# Function to close the database connection
def close_connection(conn):
    conn.close()

#customers table -----------------------------------------------------------------------------------------

# Function to create the customer table
def create_customer_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY,
        password TEXT NOT NULL,
        first_name TEXT NOT NULL,
        surname TEXT NOT NULL,
        email TEXT NOT NULL,
        address TEXT NOT NULL
    )
    ''')
    conn.commit()

# Function to generate a unique random 5-digit ID
def generate_customer_id():
    id = random.randint(10000, 99999)
    while True:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customers WHERE id = ?", (id,))
        if cursor.fetchone() is None:
            break
        id = random.randint(10000, 99999)
    return id

# Function to insert a customer into the database
def new_customer(conn, c_id, password, first_name, surname, email, address):
    cursor = conn.cursor()
    customer_data = (c_id, password, first_name, surname, email, address)
    
    cursor.execute('''
    INSERT INTO customers (id, password, first_name, surname, email, address)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', customer_data)
    conn.commit()

def check_customer_login(conn, customer_id, password):
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM customers WHERE id = ? AND password = ?
    ''', (customer_id, password))
    return cursor.fetchone()


#librarians table -----------------------------------------------------------------------------------------

def create_librarian_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS librarians(
        id INTEGER PRIMARY KEY,
        password TEXT NOT NULL,
        first_name TEXT NOT NULL,
        surname TEXT NOT NULL,
        email TEXT NOT NULL,
        address TEXT NOT NULL
    )
    ''')

    conn.commit()

# Function to generate a unique random 5-digit ID
def generate_librarian_id():
    id = random.randint(10000, 99999)
    while True:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM librarians WHERE id = ?", (id,))
        if cursor.fetchone() is None:
            break
        id = random.randint(10000, 99999)
    return id

def new_librarian(conn, l_id, password, first_name, surname, email, address):
    cursor = conn.cursor()
    librarian_data = (l_id, password, first_name, surname, email, address)

    cursor.execute('''
    INSERT INTO librarians (id, password, first_name, surname, email, address)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', librarian_data)
    conn.commit()

def check_librarian_login(conn, librarian_id, password):
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM librarians WHERE id = ? AND password = ?
    ''', (librarian_id, password))
    return cursor.fetchone()



# # Main function to run the program
# def main():
#     # Connect to the database
#     conn = connect_to_db()

#     # Create the customer table
#     create_librarian_table(conn)

#     # Insert a customer (Example data)
#     new_librarian(conn, 'prova pass 5', 'prova nome 5', 'prova cogn 5', 'provae5@email.com', 'prova strada 5')

#     # Close the connection
#     close_connection(conn)
#     print("Librarian table created and data inserted!")

# # Run the program
# if __name__ == "__main__":
#     main()