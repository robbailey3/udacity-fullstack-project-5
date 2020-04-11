import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS
from flask_swagger import swagger
from .models.models import db_drop_and_create_all, setup_db, db, Actor, Agent, Movie
from .exceptions import BadRequestException
import time


def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    SWAGGER_URL = '/docs'
    API_URL = 'http://localhost:5000'

    swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={  # Swagger UI config overrides
        'app_name': 'Hello World'

    })

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, POST, PATCH, PUT, DELETE, OPTIONS')
        return response

    @app.route('/')
    def spec():
        '''
        Get swagger JSON documentation
        ---
        tags:
          - Root

        responses:
          200:
            description: Returns the JSON swagger documentation
        '''
        swag = swagger(app)
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "Capstone API"
        return jsonify(swag)

    # GET Routes
    @app.route('/actors')
    def get_actors():
        '''
        Get all Actors
        ---
        tags:
          - Actors

        responses:
          200:
            description: Returns an array of actors
        '''
        actors = Actor.query.all()
        actors = [actor.format() for actor in actors]
        return jsonify({"result": actors, "timestamp": time.time(), "success": True})

    @app.route('/movies')
    def get_movies():
        '''
        Get all Movies
        ---
        tags:
          - Movies

        responses:
          200:
            description: Returns an array of Movies
        '''
        movies = Movie.query.all()
        movies = [movie.format() for movie in movies]
        return jsonify({"result": movies, "timestamp": time.time(), "success": True})

    @app.route('/agents')
    def get_agents():
        '''
        Get all Agents
        ---
        tags:
          - Agents

        responses:
          200:
            description: Returns an array of Agents
        '''
        agents = Agent.query.all()
        agents = [agent.format() for agent in agents]
        return jsonify({"result": agents, "timestamp": time.time(), "success": True})

    # GET by ID routes

    @app.route('/actors/<int:actor_id>')
    def get_actor_by_id(actor_id):
        '''
        Get a single actor by their ID
        ---
        tags:
          - Actors
        parameters:
            - name: actor_id
              in: path
              description: The ID of the Actor to retrieve
              required: true
              type: number

        responses:
          200:
            description: Returns a single Actor
        '''
        actor = Actor.query.filter(Actor.id == actor_id).first()
        if actor is None:
            return jsonify({"timestamp": time.time(), "success": True, "result": []})
        actor = actor.format()
        return jsonify({"timestamp": time.time(), "success": True, "result": actor})

    @app.route('/movies/<int:movie_id>')
    def get_movie_by_id(movie_id):
        '''
        Get a single movie by its ID
        ---
        tags:
          - Movies
        parameters:
            - name: movie_id
              in: path
              description: The ID of the Movie to retrieve
              required: true
              type: number

        responses:
          200:
            description: Returns a single Movie
        '''
        movie = Movie.query.filter(Movie.id == movie_id).first()
        if movie is None:
            return jsonify({"timestamp": time.time(), "success": True, "result": []})
        movie = movie.format()
        return jsonify({"timestamp": time.time(), "success": True, "result": movie})

    @app.route('/agents/<int:agent_id>')
    def get_agent_by_id(agent_id):
        '''
        Get a single Agent by its ID
        ---
        tags:
          - Agents
        parameters:
            - name: agent_id
              in: path
              description: The ID of the Agent to retrieve
              required: true
              type: number

        responses:
          200:
            description: Returns a single Agent
        '''
        agent = Agent.query.filter(Agent.id == agent_id).first()
        if agent is None:
            return jsonify({"timestamp": time.time(), "success": True, "result": []})
        agent = agent.format()
        return jsonify({"timestamp": time.time(), "success": True, "result": agent})

    @app.route('/actors', methods=["POST"])
    def create_new_actor():
        try:
            body = request.get_json()
            if body is None:
                raise BadRequestException()
            user_input = {
                "name": body.get('name', None),
                "age": body.get('age', None),
                "gender": body.get('gender', None),
                "headshot_url": body.get('headshot_url', None),
                "agent_id": body.get('agent_id', None)
            }
            actor = Actor(name=user_input['name'], age=user_input['age'], gender=user_input['gender'],
                          headshot_url=user_input['headshot_url'], agent_id=user_input['agent_id'])
            db.session.add(actor)
            db.session.commit()
            return jsonify({"success": True, "result": actor.format(), "timestamp": time.time()}), 201
        except BadRequestException as err:
            abort(400)
        except Exception as err:
            db.session.rollback()
            return jsonify({"success": False}), 500
        finally:
            db.session.close()

    @app.route('/agents', methods=["POST"])
    def create_new_agent():
        try:
            body = request.get_json()

            if body is None:
                abort(400)

            user_input = {
                "name": body.get('name', None),
                "phone_number": body.get('phone_number', None),
                "email": body.get('email', None)
            }
            agent = Agent(
                name=user_input['name'], phone_number=user_input['phone_number'], email=user_input['email'])

            db.session.add(agent)
            db.session.commit()

            return jsonify({"success": True, "result": agent.format(), "timestamp": time.time()}), 201
        except Exception as err:
            db.session.rollback()
            return jsonify({"success": False, "error": str(err)}), 500

        finally:
            db.session.close()

    @app.route('/movies', methods=["POST"])
    def create_new_movie():
        try:
            body = request.get_json()

            if body is None:
                abort(400)

            user_input = {
                "title": body.get('title', None),
                "release_date": body.get('release_date', None)
            }
            movie = Movie(
                title=user_input['title'], release_date=user_input['release_date'])

            db.session.add(movie)
            db.session.commit()

            return jsonify({"success": True, "result": movie.format(), "timestamp": time.time()}), 201
        except Exception as err:
            db.session.rollback()
            return jsonify({"success": False, "error": str(err)}), 500

        finally:
            db.session.close()

    @app.route('/actors/<int:id>', methods=["PATCH"])
    def update_actor(id):
        try:
            body = request.get_json()

            if body is None:
                abort(400)

            actor = Actor.query.filter(Actor.id == id).first()

            if actor is None:
                abort(400)

            user_input = {
                "name": body.get('name', actor.name),
                "age": body.get('age', actor.age),
                "gender": body.get('gender', actor.gender),
                "headshot_url": body.get('headshot_url', actor.headshot_url),
                "agent_id": body.get('agent_id', actor.agent_id)
            }

            actor.name = user_input['name']
            actor.age = user_input['age']
            actor.gender = user_input['gender']
            actor.headshot_url = user_input['headshot_url'],
            actor.agent_id = user_input['agent_id']

            actor.update()

            return jsonify({"success": True, "result": actor.format(), "timestamp": time.time()}), 200

        except Exception as err:
            db.session.rollback()
            return jsonify({"success": False, "error": str(err)}), 500

        finally:
            db.session.close()

    @app.route('/agents/<int:id>', methods=["PATCH"])
    def update_agent(id):
        try:
            body = request.get_json()

            if body is None:
                abort(400)

            agent = Agent.query.filter(Agent.id == id).first()

            if agent is None:
                abort(400)

            user_input = {
                "name": body.get('name', agent.name),
                "email": body.get('email', agent.email),
                "phone_number": body.get('phone_number', agent.phone_number),
            }

            agent.name = user_input['name']
            agent.phone_number = user_input['phone_number']
            agent.email = user_input['email']

            agent.update()

            return jsonify({"success": True, "result": agent.format(), "timestamp": time.time()}), 200

        except Exception as err:
            db.session.rollback()
            return jsonify({"success": False, "error": str(err)}), 500

        finally:
            db.session.close()

    @app.route('/movies/<int:id>', methods=["PATCH"])
    def update_movie(id):
        try:
            body = request.get_json()

            if body is None:
                abort(400)

            movie = Movie.query.filter(Movie.id == id).first()

            if movie is None:
                abort(400)

            user_input = {
                "title": body.get('title', movie.title),
                "release_date": body.get('release_date', movie.release_date)
            }

            movie.title = user_input['title']
            movie.release_date = user_input['release_date']

            movie.update()

            return jsonify({"success": True, "result": movie.format(), "timestamp": time.time()}), 200

        except Exception as err:
            db.session.rollback()
            return jsonify({"success": False, "error": str(err)}), 500

        finally:
            db.session.close()

    @app.route('/actors/<int:id>', methods=["DELETE"])
    def delete_actor(id):
        try:
            actor = Actor.query.filter(Actor.id == id).first()
            if actor is None:
                raise BadRequestException('No actor found with ID %i' % (id))
            actor.delete()
            return jsonify({"success": True, "timestamp": time.time()}), 200
        except BadRequestException as err:
            db.session.rollback()
            abort(400, err)
        except Exception as err:
            db.session.rollback()
            abort(500)
        finally:
            db.session.close()

    @app.route('/agents/<int:id>', methods=["DELETE"])
    def delete_agent(id):
        try:
            agent = Agent.query.filter(Agent.id == id).first()
            if agent is None:
                raise BadRequestException()
            agent.delete()
            return jsonify({"success": True, "timestamp": time.time()}), 200

        except BadRequestException:
            db.session.rollback()
            abort(400)
        except Exception as err:
            db.session.rollback()
            abort(500)
        finally:
            db.session.close()

    @app.route('/movies/<int:id>', methods=["DELETE"])
    def delete_movie(id):
        try:
            movie = Movie.query.filter(Movie.id == id).first()
            if movie is None:
                raise BadRequestException()
            movie.delete()
            return jsonify({"success": True, "timestamp": time.time()}), 200

        except BadRequestException:
            db.session.rollback()
            abort(400)
        except Exception as err:
            db.session.rollback()
            abort(500)
        finally:
            db.session.close()

    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    # Error Handling
    '''
    Example error handling for unprocessable entity
    '''
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unprocessable"
        }), 422

    @app.errorhandler(404)
    def page_not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Route not found"
        }), 404

    @app.errorhandler(401)
    def user_unauthenticated(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "User not authenticated"
        }), 401

    @app.errorhandler(400)
    def invalid_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": str(error)
        }), 400

    # @app.errorhandler(AuthError)
    # def user_is_unauthenticated(error):
    #     return jsonify({
    #         "success": False,
    #         "error": 401,
    #         "message": "User not authenticated"
    #     }), 401
    return app


app = create_app()

if __name__ == '__main__':
    app.run()
