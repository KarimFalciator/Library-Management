import sqlite3
import random

def create_database():
    conn = sqlite3.connect('customers.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY,
        password TEXT,
        first_name TEXT,
        surname TEXT,
        email TEXT,
        address TEXT
    )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def generate_customer_id():
    while True:
        customer_id = random.randint(10000, 99999)
        conn = sqlite3.connect('customers.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM customers WHERE id = ?', (customer_id,))
        if cursor.fetchone() is None:
            conn.close()
            return customer_id
        conn.close()

def add_customer(password, first_name, surname, email, address):
    conn = sqlite3.connect('customers.db')
    cursor = conn.cursor()
    
    customer_id = generate_customer_id()

    cursor.execute('''
    INSERT INTO customers (id, password, first_name, surname, email, address)
    VALUES (?, ?, ?, ?, ?, ?)''', (customer_id, password, first_name, surname, email, address))
    
    conn.commit()
    conn.close()

def get_customer_by_id(customer_id):
    conn = sqlite3.connect('customers.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM customers WHERE id = ?', (customer_id,))
    customer = cursor.fetchone()
    conn.close()
    return customer

# Create the database and table
create_database()