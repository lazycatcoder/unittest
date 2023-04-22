import sqlite3


class Customers:
    def __init__(self):
        # Initialize the class object, connect to the database and create a cursor
        self.connection = sqlite3.connect('customers.db')
        self.cursor = self.connection.cursor()

        # Create the "customers" table if it doesn't already exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT,
                email TEXT,
                phone TEXT,
                country TEXT
            )
        ''')
        self.connection.commit()

    def add_customer(self, first_name, last_name, email, phone, country):
        # Method for adding a new client to the database
        self.cursor.execute('''
            INSERT INTO customers (first_name, last_name, email, phone, country)
            VALUES (?, ?, ?, ?, ?)
        ''', (first_name, last_name, email, phone, country))
        self.connection.commit()
        print("Customer added successfully.")

    def find_customers_by_name(self, first_name, last_name):
        # Method to search for clients by name in the database
        self.cursor.execute('''
            SELECT *
            FROM customers
            WHERE first_name LIKE ? AND last_name LIKE ?
            ORDER BY first_name, last_name
        ''', ('%' + first_name + '%', '%' + last_name + '%'))
        rows = self.cursor.fetchall()
        if rows:
            result = []
            for row in rows:
                result.append(row)
            return result
        else:
            print("No customers found by name.")
            return []  # Return an empty list if no clients are found

    def find_customers_by_country(self, country):
        # Method to search for customers by country in the database using a generator
        self.cursor.execute('''
            SELECT *
            FROM customers
            WHERE country LIKE ?
            ORDER BY first_name, last_name
        ''', ('%' + country + '%',))
        rows = self.cursor.fetchall()
        if rows:
            result = []
            for row in rows:
                result.append(row)
            return result  # Return a list with found clients
        else:
            print("No customers found by country.")
            return []  # Return an empty list if no clients are found
        
    def __del__(self):
       # Closing the cursor and the database connection when the class object is deleted
        self.cursor.close()
        self.connection.close()