from flask import jsonify
from api.lib.db import *
from api.models import movie
# from backend.api.models.movie import Movie 
# from  ..models.movie import Movie


class Actor: 
    columns = ['id', 'name']
    __table__ = 'actors'

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise f'{key} not in {self.columns}' 
        for k, v in kwargs.items():
            setattr(self, k, v)

    def movies(self, conn): 
        cursor = conn.cursor()
        cursor.execute('select * from movies join movie_actors on movie_actors.movie_id = movies.id join actors on actors.id = movie_actors.actor_id where actors.id = %s', (self.id, ))
        movie_records = cursor.fetchall()
        # return None
        return build_from_records(movie.Movie, movie_records) 

    def to_json(self, conn): 
        actor_json = self.__dict__
        movies = self.movies(conn)
        actor_json['movies'] = [movie.__dict__ for movie in movies]
        return actor_json