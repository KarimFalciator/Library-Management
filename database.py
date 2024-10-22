import sqlite3
import random
from datetime import datetime, timedelta

# Function to connect to the SQLite database
def connect_to_db(db_name='lending.db'):
    conn = sqlite3.connect(db_name)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

# Function to close the database connection
def close_connection(conn):
    conn.close()

# Students table -----------------------------------------------------------------------------------------

# Function to create the customer table
def create_students_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students(
        s_id INTEGER PRIMARY KEY,
        s_fname TEXT NOT NULL,
        s_lname TEXT NOT NULL,
        s_email TEXT NOT NULL,
        s_number TEXT NOT NULL
    )
    ''')
    conn.commit()

# Function to generate a unique random 6-digit ID
def generate_student_id():
    s_id = random.randint(100000, 999999)
    while True:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE s_id = ?", (s_id,))
        if cursor.fetchone() is None:
            break
        s_id = random.randint(100000, 999999)
    return s_id

# Function to insert a student into the database
def new_student(conn, s_fname, s_lname, s_email, s_number):
    s_id = generate_student_id()
    cursor = conn.cursor()
    student_data = (s_id, s_fname, s_lname, s_email, s_number)
    
    cursor.execute('''
    INSERT INTO students (s_id, s_fname, s_lname, s_email, s_number)
    VALUES (?, ?, ?, ?, ?)
    ''', student_data)
    conn.commit()

# Function to check if a customer exists in the database
def check_student(conn, s_id):
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM students WHERE s_id = ?
    ''', (s_id,))
    return cursor.fetchone()

def check_s_email(conn, s_id, s_email):
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM students WHERE s_id = ? AND s_email = ?
    ''', (s_id, s_email,))
    return cursor.fetchone()


# Teachers table -----------------------------------------------------------------------------------------

# Function to create the teachers table
def create_teachers_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS teachers(
        t_id INTEGER PRIMARY KEY,
        t_pass TEXT NOT NULL,
        t_fname TEXT NOT NULL,
        t_lname TEXT NOT NULL,
        t_email TEXT NOT NULL
    )
    ''')

    conn.commit()

# Function to generate a unique random 6-digit ID
def generate_teacher_id():
    t_id = random.randint(100000, 999999)
    while True:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM teachers WHERE t_id = ?", (t_id,))
        if cursor.fetchone() is None:
            break
        t_id = random.randint(100000, 999999)
    return t_id

def new_teacher(conn, t_id, t_pass, t_fname, t_lname, t_email):
    cursor = conn.cursor()
    t_data = (t_id, t_pass, t_fname, t_lname, t_email)

    cursor.execute('''
    INSERT INTO teachers (t_id, t_pass, t_fname, t_lname, t_email)
    VALUES (?, ?, ?, ?, ?)
    ''', t_data)
    conn.commit()

def check_teacher_login(conn, t_id, t_pass):
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM teachers WHERE t_id = ? AND t_pass = ?
    ''', (t_id, t_pass))
    return cursor.fetchone()

def check_t_email(conn, t_id, t_email):
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM teachers WHERE t_id= ? AND t_email= ?
    ''', (t_id, t_email))
    return cursor.fetchone()

# def update_OTP(conn, t_id, OTP):
#     cursor = conn.cursor()
#     cursor.execute('''
#     UPDATE teachers SET t_OTP = ? WHERE t_id = ?
#     ''', (OTP, t_id))
#     conn.commit()

def update_teacher_password(conn, t_id, t_pass):
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE teachers SET t_pass = ? WHERE t_id = ?
    ''', (t_pass, t_id))
    conn.commit()

# Resources table -----------------------------------------------------------------------------------------

# Function to create the resources table
def create_resources_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS resources (
        r_id INTEGER PRIMARY KEY AUTOINCREMENT,
        r_name TEXT NOT NULL,
        r_subject TEXT default NULL,
        r_qty INTEGER default 1
    )
    ''')
    conn.commit()

# Function to insert a resource into the database
def new_resource(conn, r_name, r_qty=1):
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM resources WHERE r_name = ?
        ''', (r_name,))
    resource = cursor.fetchone()
    if resource:
        cursor.execute('''UPDATE resources SET r_qty = r_qty + ? WHERE r_name = ?
        ''', (r_qty, r_name))
    else:
        cursor.execute('''INSERT INTO resources (r_name, r_qty) VALUES (?, ?)
        ''', (r_name, r_qty))
    conn.commit()

# Function to check if a resource exists in the database
def check_resource(conn, r_id):
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM resources WHERE r_id = ?
    ''', (r_id,))
    resource = cursor.fetchone()
    r_qty = resource[3]
    if resource and r_qty > 0:
        return True
    else:
        return False


# Borrowed table -----------------------------------------------------------------------------------------

# Function to create the borrowed table
def create_borrowed_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS borrowed (
        ref INTEGER PRIMARY KEY AUTOINCREMENT,
        s_id INTEGER NOT NULL,
        r_id INTEGER NOT NULL,
        b_date TEXT NOT NULL,
        d_date TEXT NOT NULL,
        r_date TEXT DEFAULT NULL,
        FOREIGN KEY (s_id) REFERENCES students(s_id),
        FOREIGN KEY (r_id) REFERENCES resources(r_id)
    )
    ''')
    conn.commit()

# Function to insert a new borrowed resource into the database
def new_borrowed(conn, s_id, r_id):
    conn = conn
    r_id = r_id
    cursor = conn.cursor()
    b_date = datetime.now().strftime("%Y-%m-%d")
    d_date = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')
    r_date = None
    borrowed_data = (s_id, r_id, b_date, d_date, r_date)
    
    if check_resource(conn, r_id):
        cursor.execute('''
        INSERT INTO borrowed (s_id, r_id, b_date, d_date, r_date)
        VALUES (?, ?, ?, ?, ?)
        ''', borrowed_data)
        conn.commit()
        return True
    else:
        return False


# Function to return a borrowed resource
def return_borrowed(conn, ref):
    cursor = conn.cursor()
    r_date = datetime.now().strftime('%D-%M-%Y')
    cursor.execute('''
    UPDATE borrowed SET r_date = ? WHERE ref = ?
    ''', (r_date, ref))
    conn.commit()

# Function to get all borrowed resources
def get_all_borrowed(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT ref, s_id, r_id, b_date, d_date, r_date FROM borrowed')
    return cursor.fetchall()

# Function to check if a customer exists in the database
def check_borrowed(conn, ref):
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM students WHERE ref = ?
    ''', (ref,))
    return cursor.fetchone()

# Function to get the last ref from borrowed table
def get_last_ref(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT MAX(ref) FROM borrowed')
    return cursor.fetchone()[0]


# Main function to run the program
def main():
    # Connect to the database
    conn = connect_to_db()

    # Create the tables
    create_teachers_table(conn)
    create_students_table(conn)
    create_resources_table(conn)
    create_borrowed_table(conn)

    # Insert a new record in every table
    # new_teacher(conn, 111111, 'Lepassword1', 'Karim', 'Soliman', 'karimfalciator@gmail.com')
    # new_student(conn, 'Nome1', 'Cognome1', 'email1', 'nummero1')
    new_resource(conn, '111111')
    new_borrowed(conn, 376594, 1)

    # Close the connection
    close_connection(conn)

# Run the program
if __name__ == "__main__":
    main()