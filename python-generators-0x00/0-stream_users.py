import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Connect to the ALX_prodev database
def connect_to_prodev():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database="ALX_prodev"
        )
        print("Connected to ALX_prodev database")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Generator function to stream rows from the user_data table
def stream_users():
    connection = connect_to_prodev()
    if not connection:
        return
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data")
        for row in cursor:
            yield row
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        connection.close()

