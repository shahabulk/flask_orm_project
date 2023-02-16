from flask import Flask, jsonify
import psycopg2 
from lib.db import conn
app = Flask()
app.config.from_mapping()

@app.route('/')
def home():
    return 'silliness'

@app.route('/movies')
def movies():
    cursor = conn.cursor()
def create_app(db_name, username, password):
