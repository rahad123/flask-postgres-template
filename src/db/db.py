import psycopg2
from flask import Flask, render_template

app = Flask(__name__)

# Define the connection parameters
params = {
    'database': 'Match360',
    'user': 'postgres',
    'password': 'Billu_1234',
    'host': 'localhost',
    'port': '5432'
}

try:
    # Attempt to establish a connection
    conn = psycopg2.connect(**params)
    print("Connected to PostgreSQL")
except psycopg2.Error as e:
    print("Error: Unable to connect to PostgreSQL")
    print(e)
