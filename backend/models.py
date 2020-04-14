import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
import os

db_url = os.environ['DATABASE_URL']
db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=db_url):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()


association_table = db.Table('actors_movies', db.Model.metadata,
                             Column('movie_id', Integer,
                                    db.ForeignKey('movies.id')),
                             Column('actor_id', Integer,
                                    db.ForeignKey('actors.id'))
                             )


class Actor(db.Model):
    __tablename__ = 'actors'

    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    gender = db.Column(db.String)
    headshot_url = db.Column(db.String)
    agent_id = db.Column(db.Integer, db.ForeignKey('agents.id'))
    agent = db.relationship("Agent", back_populates="actors")
    movies = db.relationship(
        'Movie', secondary=association_table, back_populates="actors")

    def format(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "headshot_url": self.headshot_url,
            "agent_id": self.agent_id,
            "movies": [movie.format_short() for movie in self.movies]
        }

    def format_short(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "headshot_url": self.headshot_url,
            "agent_id": self.agent_id,
        }

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()


class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    release_date = db.Column(db.DateTime)
    synopsis = db.Column(db.String)
    rating = db.Column(db.Float)
    actors = db.relationship(
        'Actor', secondary=association_table, back_populates="movies")

    def format(self):
        return {
            "id": self.id,
            "title": self.title,
            "release_date": self.release_date,
            "actors": [actor.format_short() for actor in self.actors]
        }

    def format_short(self):
        return {
            "id": self.id,
            "title": self.title,
            "release_date": self.release_date,
        }

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()


class Agent(db.Model):
    __tablename__ = 'agents'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    actors = db.relationship('Actor')
    phone_number = db.Column(db.String)
    email = db.Column(db.String)

    def format(self):
        return {
            "id": self.id,
            "name": self.name,
            "actors": [actor.format_short() for actor in self.actors],
            "phone_number": self.phone_number,
            "email": self.email
        }

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
