import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="LockDown@513",  # <-- replace this with your actual MySQL root password
        database="clinic_db"  # The database created in MySQL
    )
