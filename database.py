import mysql.connector as sql
from mysql.connector import Error

def create_connection():
    conn = None
    try:
        conn = sql.connect(
            host="localhost",
            user="root",
            password="Yagya@2003",
            database="finance"
        )
        if not conn.is_connected():
            print("Connection not established")
            return None
        else:
            print("Connection established successfully!")
    except Error as err:
        print(f"Error: {err}")
    return conn

def create_table(conn):
    query = """
        CREATE TABLE IF NOT EXISTS expenditure (
          id INT AUTO_INCREMENT PRIMARY KEY,
          category VARCHAR(50) NOT NULL,
          description VARCHAR(200),
          date DATE NOT NULL,
          amount DECIMAL(10,2) NOT NULL
        )
    """
    cr = conn.cursor()
    try:
        cr.execute(query)
        print("Table created successfully!")
    except Error as err:
        print(f"Error: {err}")

def add_expenses(conn, expense):
    query = "INSERT INTO expenditure (category, description, date, amount) VALUES (%s, %s, %s, %s)"
    cr = conn.cursor()
    try:
        cr.execute(query, expense)
        conn.commit()
        print("Expense added successfully!")
    except Error as err:
        print(f"Error: {err}")

def fetch_all(conn):
    cr = conn.cursor()
    query = "SELECT * FROM expenditure"
    cr.execute(query)
    rows = cr.fetchall()
    return rows
