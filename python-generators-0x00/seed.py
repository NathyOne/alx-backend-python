import mysql.connector
from mysql.connector import Error


def create_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            database="ALX_prodev",
            user="root",
            password="root",
            port="3306"
        )
        if conn.is_connected():
            print("connected!")
            return conn
    except Error as e:
        print(f"Error connecting to mysql: {e}")
        return None


connection = create_connection()

if connection:
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM user_data")

        # Fetch and display results
        results = cursor.fetchall()
        print(f"Found {len(results)} records:")

        for row in results:
            print(row)

    except Error as e:
        print(f"Error executing query: {e}")

    finally:
        # Ensure connection is closed
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed")
else:
    print("Failed to establish database connection")
