import psycopg2
from flask import Flask, render_template
from src.config.config import DB_NAME, DB_USER, DB_PASS, DB_HOST, DB_PORT

app = Flask(__name__)

# Define the connection parameters
params = {
    'database': DB_NAME,
    'user': DB_USER,
    'password': DB_PASS,
    'host': DB_HOST,
    'port': DB_PORT,
}

try:
    # Attempt to establish a connection
    conn = psycopg2.connect(**params)
    print("Connected to PostgreSQL")
except psycopg2.Error as e:
    print("Error: Unable to connect to PostgreSQL")
    print(e)
