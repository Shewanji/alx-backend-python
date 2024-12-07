import mysql.connector
import csv
import os
import uuid
from dotenv import load_dotenv

load_dotenv()

# Connect to MySQL server
def connect_db():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        print("Connected to MySQL server")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Create the database if it doesn't exist
def create_database(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        print("Database ALX_prodev created or already exists")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

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

# Create the user_data table
def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS user_data (
                user_id CHAR(36) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age DECIMAL(3, 0) NOT NULL
            ) ENGINE=InnoDB;
            """
        )
        print("Table user_data created successfully")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Insert data into the user_data table
def insert_data(connection, data):
    try:
        cursor = connection.cursor()
        with open(data, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                user_id = str(uuid.uuid4())  
                name = row['name']
                email = row['email']
                age = int(row['age'])
                cursor.execute(
                    """
                    INSERT IGNORE INTO user_data (user_id, name, email, age)
                    VALUES (%s, %s, %s, %s)
                    """,
                    (user_id, name, email, age)
                )
        connection.commit()
        print("Data inserted successfully")
        cursor.close()
    except FileNotFoundError:
        print(f"Error: File {data} not found")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

