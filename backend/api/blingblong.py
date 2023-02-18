from flask import Flask, jsonify
import psycopg2 
from api.lib.db import *
from api.models.movie import *
from api.lib.settings import *
# from api.lib.db import conn, build_from_record, find
# from api.models.movie import *
# import api.models.movie as tyson
# import api.lib.db as mike



def create_app(dbname, user, password, is_prod = True):
    app = Flask(__name__)
    #change is_prod if:
    @app.route('/')
    def home():
        return 'Welcome to the movies api'

    @app.route('/movies')
    def movies():
        if is_prod: 
            current_app.config['DB_PASSWORD'] = DB_PASSWORD
            current_app.config['DB_USER'] = DB_USER
            current_app.config['DATABASE'] = DB_NAME
            conn = psycopg2.connect(user = current_app.config['DB_USER'],
                                    password = current_app.config['DB_PASSWORD'],
                                    dbname = current_app.config['DATABASE'])
            cursor = conn.cursor()
            cursor.execute('select * from movies;')
            movies = find_all(Movie, conn)
            movie_jsons = [movie.to_json(conn) for movie in movies]
            return jsonify(movie_jsons)
        
        else: 
            current_app.config['TEST_DB_USER'] = TEST_DB_USER
            current_app.config['TEST_DB_PASSWORD'] = TEST_DB_PASSWORD
            current_app.config['TEST_DB_NAME'] = TEST_DB_NAME    
            conn = psycopg2.connect(user = current_app.config['TEST_DB_USER'],
                                    password = current_app.config['TEST_DB_PASSWORD'],
                                    dbname = current_app.config['TEST_DB_NAME'])
            cursor = conn.cursor()
            cursor.execute('select * from movies;')
            movies = find_all(Movie, conn)
            movie_jsons = [movie.to_json(conn) for movie in movies]
            # movie_dicts = [movie.__dict__ for movie in movies]
            return jsonify(movie_jsons)
    
    @app.route('/movies/<id>')
    def movie(id):
        if is_prod:
            current_app.config['DB_PASSWORD'] = DB_PASSWORD
            current_app.config['DB_USER'] = DB_USER
            current_app.config['DATABASE'] = DB_NAME
            # conn = psycopg2.connect(dbname = TEST_DB_NAME, user = TEST_DB_USER,  password = TEST_DB_PASSWORD)
            # cursor = conn.cursor()
            conn = psycopg2.connect(user = current_app.config['DB_USER'],
                                    password = current_app.config['DB_PASSWORD'],
                                    dbname = current_app.config['DATABASE'])
            movie = find(Movie, id, conn)
            movie_json = movie.to_json(conn)
            # movie_json['actors'] = movie.actors() 
            # cursor.execute('select * from movies where movies.id = %s;', (id,))
            # movie_record = cursor.fetchone()
            # movie = build_from_record(Movie, movie_record)
            return jsonify(movie_json)
            
        else:
            # conn = psycopg2.connect(dbname = TEST_DB_NAME, user = TEST_DB_USER,  password = TEST_DB_PASSWORD)
            # cursor = conn.cursor()
            current_app.config['TEST_DB_USER'] = TEST_DB_USER
            current_app.config['TEST_DB_PASSWORD'] = TEST_DB_PASSWORD
            current_app.config['TEST_DB_NAME'] = TEST_DB_NAME
            conn = psycopg2.connect(user = current_app.config['TEST_DB_USER'],
                                    password = current_app.config['TEST_DB_PASSWORD'],
                                    dbname = current_app.config['TEST_DB_NAME'])
            movie = find(Movie, id, conn)
            movie_json = movie.to_json(conn)
            # movie_json['actors'] = movie.actors() 
            # cursor.execute('select * from movies where movies.id = %s;', (id,))
            # movie_record = cursor.fetchone()
            # movie = build_from_record(Movie, movie_record)
            print(movie_json)
            return jsonify(movie_json)


    @app.route('/actors') 
    def actors(): 
        if is_prod: 
            current_app.config['DB_PASSWORD'] = DB_PASSWORD
            current_app.config['DB_USER'] = DB_USER
            current_app.config['DATABASE'] = DB_NAME
            conn = psycopg2.connect(user = current_app.config['DB_USER'],
                                    password = current_app.config['DB_PASSWORD'],
                                    dbname = current_app.config['DATABASE'])

            cursor = conn.cursor()
            cursor.execute('select * from actors;')
            actors = find_all(Actor, conn)
            actor_jsons = [actor.to_json(conn) for actor in actors]
            return jsonify(actor_jsons)
        
        else:
            current_app.config['TEST_DB_USER'] = TEST_DB_USER
            current_app.config['TEST_DB_PASSWORD'] = TEST_DB_PASSWORD
            current_app.config['TEST_DB_NAME'] = TEST_DB_NAME
            conn = psycopg2.connect(user = current_app.config['TEST_DB_USER'],
                                    password = current_app.config['TEST_DB_PASSWORD'],
                                    dbname = current_app.config['TEST_DB_NAME'])

            cursor = conn.cursor()
            cursor.execute('select * from actors;')
            actors = find_all(Actor, conn)
             
            actor_jsons = [actor.to_json(conn) for actor in actors]
            return jsonify(actor_jsons)

        # conn = get_db()
        # cursor = conn.cursor()
        # cursor.execute('select * from movies;')
        # movies = find_all(Movie, conn)
        # movie_dicts = [movie.__dict__ for movie in movies]
        # return jsonify(movie_dicts)

    @app.route('/actors/<id>') 
    def actor(id):
        if is_prod:
            current_app.config['DB_PASSWORD'] = DB_PASSWORD
            current_app.config['DB_USER'] = DB_USER
            current_app.config['DATABASE'] = DB_NAME
            conn = psycopg2.connect(user = current_app.config['DB_USER'],
                                    password = current_app.config['DB_PASSWORD'],
                                    dbname = current_app.config['DATABASE'])

            actor = find(Actor, id, conn)
            actor_json = actor.to_json(conn)

            return jsonify(actor_json)
        
        else: 
            current_app.config['TEST_DB_USER'] = TEST_DB_USER
            current_app.config['TEST_DB_PASSWORD'] = TEST_DB_PASSWORD
            current_app.config['TEST_DB_NAME'] = TEST_DB_NAME
            conn = psycopg2.connect(user = current_app.config['TEST_DB_USER'],
                                    password = current_app.config['TEST_DB_PASSWORD'],
                                    dbname = current_app.config['TEST_DB_NAME'])

            actor = find(Actor, id, conn)
            actor_json = actor.to_json(conn)

            return jsonify(actor_json)

    

    return app