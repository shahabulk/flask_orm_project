from flask import Flask, jsonify
import psycopg2 
from api.lib.db import conn, build_from_record, find
from api.models.movie import *
# from api.lib.db import conn, build_from_record, find
# from api.models.movie import *
# import api.models.movie as tyson
# import api.lib.db as mike



def create_app(dbname, user, password):
    app = Flask(__name__)

    @app.route('/')
    def home():
        return 'silliness'

    @app.route('/movies')
    def movies():
        conn = psycopg2.connect(dbname = DB_NAME, user = DB_USER,  password = DB_PASSWORD)
        cursor = conn.cursor()
        # cursor.execute('select * from movies;')
        movies = find_all(Movie, conn)
        movie_dicts = [movie.__dict__ for movie in movies]
        return jsonify(movie_dicts)
    
    @app.route('/movies/<id>')
    def movie(id):
        conn = psycopg2.connect(dbname = DB_NAME, user = DB_USER,  password = DB_PASSWORD)
        cursor = conn.cursor()
        movie = find(Movie, id, conn)
        # cursor.execute('select * from movies where movies.id = %s;', (id,))
        # movie_record = cursor.fetchone()
        # movie = build_from_record(Movie, movie_record)
        return jsonify(movie.__dict__)

    

    return app