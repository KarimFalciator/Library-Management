import sqlite3
import random


# Function to connect to the SQLite database
def connect_to_db(db_name='library.db'):
    return sqlite3.connect(db_name)

# Function to close the database connection
def close_connection(conn):
    conn.close()

#customers table -----------------------------------------------------------------------------------------

# Function to create the customer table
def create_students_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        s_id INTEGER PRIMARY KEY,
        f_name TEXT NOT NULL,
        s_name TEXT NOT NULL,
        email TEXT NOT NULL,
        address TEXT NOT NULL,
        number TEXT NOT NULL
    )
    ''')
    conn.commit()

# # Function to generate a unique random 5-digit ID
# def generate_user_id():
#     id = random.randint(10000, 99999)
#     while True:
#         conn = connect_to_db()
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM users WHERE id = ?", (id,))
#         if cursor.fetchone() is None:
#             break
#         id = random.randint(10000, 99999)
#     return id

# Function to insert a customer into the database
def new_user(conn, s_id, f_name, s_name, email, address, number):
    cursor = conn.cursor()
    customer_data = (s_id, f_name, s_name, email, address, number)
    
    cursor.execute('''
    INSERT INTO students (s_id, f_name, s_name, email, address, number)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', customer_data)
    conn.commit()

def check_user_login(conn, s_id):
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM students WHERE id = ? AND password = ?
    ''', (s_id))
    return cursor.fetchone()


#librarians table -----------------------------------------------------------------------------------------

def create_teachers_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS teachers(
        t_id INTEGER PRIMARY KEY,
        t_password TEXT NOT NULL,
        f_name TEXT NOT NULL,
        s_name TEXT NOT NULL,
        email TEXT NOT NULL,
    )
    ''')

    conn.commit()

# Function to generate a unique random 5-digit ID
def generate_teacher_id():
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

#books table -----------------------------------------------------------------------------------------

# Function to create the books table
def create_books_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_name TEXT NOT NULL,
        available INTEGER NOT NULL,
        user_list TEXT NOT NULL DEFAULT '[]'
    )
    ''')
    conn.commit()

# Function to insert a customer into the database
def new_book(conn, book_id, name, available):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE book_id = ? AND book_name = ?", (book_id, name))
    book = cursor.fetchone()
    if book:
        cursor.execute("UPDATE books SET available = available + 1 WHERE book_id = ? AND book_name = ?", (book_id, name))
    else:
        cursor.execute("INSERT INTO books (book_id, book_name, available) VALUES (?, ?, ?)", (book_id, name, available))
    conn.commit()

def check_book(conn, book_id, book_name):
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM books WHERE book_id = ? AND book_name = ?
    ''', (book_id, book_name))
    return cursor.fetchone()



# # Main function to run the program
def main():
    # Connect to the database
    conn = connect_to_db()

    # Create the customer table
    create_users_table(conn)

    # Close the connection
    close_connection(conn)

# Run the program
if __name__ == "__main__":
    main()