import datetime 
from flask import jsonify
from api.lib.db import *
import json
from api.models.actor import Actor
class Movie:
    columns = ['id', 'title', 'studio', 'runtime', 'description', 'release_date', 'year']

    __table__ = 'movies' 

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise f'{key} not in {self.columns}' 
        for k, v in kwargs.items():
            setattr(self, k, v)

    def age(self):
        return datetime.datetime.now() - self.release_date

    def actors(self, conn):
        cursor = conn.cursor()
        cursor.execute('select * from actors join movie_actors on actors.id = movie_actors.actor_id join movies on movies.id = movie_actors.movie_id where movies.id = %s', (self.id, ))
        actors_records = cursor.fetchall()
        return build_from_records(Actor, actors_records)

    def to_json(self):
        movie_json = self.__dict__
        actors = self.actors(conn)
        movie_json['actors'] = [actor.__dict__ for actor in actors]
        return movie_json
         
 


