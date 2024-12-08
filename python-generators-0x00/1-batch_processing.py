import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Function to connect to the ALX_prodev database
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

# Generator function to fetch rows in batches
def stream_users_in_batches(batch_size):
    connection = connect_to_prodev()
    if not connection:
        return
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data")
        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield batch
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        connection.close()

# Function to process each batch and filter users over the age of 25
def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size):
        filtered_users = [user for user in batch if user['age'] > 25]
        yield filtered_users
