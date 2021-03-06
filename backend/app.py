import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS, cross_origin
from flask_swagger import swagger
from models import db_drop_and_create_all, setup_db, db, Actor, Agent, Movie
from exceptions import BadRequestException
from auth import requires_auth, AuthError
import time


def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app, supports_credentials=True)
    SWAGGER_URL = '/docs'
    API_URL = '/'

    swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={  # Swagger UI config overrides
        'app_name': 'Capstone'

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
    @requires_auth('get:actors')
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
        try:
            page_size = int(request.args.get('page-size', 50))
            offset = int(request.args.get('offset', 0))
            actors = Actor.query.order_by(Actor.id.desc()).all()
            actors = actors[offset:(page_size + offset)]
            actors = [actor.format() for actor in actors]
            return jsonify({"result": actors, "timestamp": time.time(), "success": True})
        except AuthError:
            abort(401)

    @app.route('/movies')
    @requires_auth('get:movies')
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
        try:
            page_size = int(request.args.get('page-size', 50))
            offset = int(request.args.get('offset', 0))
            movies = Movie.query.order_by(Movie.id.desc()).all()
            movies = movies[offset:(page_size+offset)]
            movies = [movie.format() for movie in movies]
            return jsonify({"result": movies, "timestamp": time.time(), "success": True})
        except AuthError:
            abort(401)

    @app.route('/agents')
    @requires_auth('get:agents')
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
        try:
            page_size = int(request.args.get('page-size', 50))
            offset = int(request.args.get('offset', 0))
            agents = Agent.query.order_by(Agent.id.desc()).all()
            agents = agents[offset:(page_size+offset)]
            agents = [agent.format() for agent in agents]
            return jsonify({"result": agents, "timestamp": time.time(), "success": True})
        except AuthError:
            abort(401)

    # GET by ID routes

    @app.route('/actors/<int:actor_id>')
    @requires_auth('get:actors')
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
        try:
            actor = Actor.query.filter(Actor.id == actor_id).first()
            if actor is None:
                return jsonify({"timestamp": time.time(), "success": True, "result": []})
            actor = actor.format()
            return jsonify({"timestamp": time.time(), "success": True, "result": actor})
        except AuthError:
            abort(401)

    @app.route('/movies/<int:movie_id>')
    @requires_auth('get:movies')
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
        try:
            movie = Movie.query.filter(Movie.id == movie_id).first()
            if movie is None:
                return jsonify({"timestamp": time.time(), "success": True, "result": []})
            movie = movie.format()
            return jsonify({"timestamp": time.time(), "success": True, "result": movie})
        except AuthError:
            abort(401)

    @app.route('/agents/<int:agent_id>')
    @requires_auth('get:agents')
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
        try:
            agent = Agent.query.filter(Agent.id == agent_id).first()
            if agent is None:
                return jsonify({"timestamp": time.time(), "success": True, "result": []})
            agent = agent.format()
            return jsonify({"timestamp": time.time(), "success": True, "result": agent})
        except AuthError:
            abort(401)

    @app.route('/actors', methods=["POST"])
    @requires_auth('post:actors')
    def create_new_actor():
        '''
        Create a new Actor
        ---
        tags:
          - Actors
        parameters:
          - name: Actor
            in: body
            schema:
              type: object
              properties:
                name:
                    type: string
                age:
                    type: number
                gender:
                    type: string
                headshot_url:
                    type: string
                agent_id:
                    type: number
                movies:
                    type: array
                    items:
                        type: number
        responses:
          201:
            description: Returns the new Actor
        '''
        try:
            body = request.get_json()

            if body is None:
                raise BadRequestException()

            user_input = {
                "name": body.get('name', None),
                "age": body.get('age', None),
                "gender": body.get('gender', None),
                "headshot_url": body.get('headshot_url', None),
                "agent_id": body.get('agent_id', None),
                "movies": body.get('movies', None)
            }

            movies = []
            if(user_input['movies'] is not None):
                for movie_id in user_input['movies']:
                    movie = Movie.query.filter(Movie.id == movie_id).first()
                    if movie is None:
                        raise BadRequestException(
                            'Movie %i not found' % (movie_id))
                    movies.append(movie)

            actor = Actor(name=user_input['name'], age=user_input['age'], gender=user_input['gender'],
                          headshot_url=user_input['headshot_url'], agent_id=user_input['agent_id'], movies=movies)

            db.session.add(actor)
            db.session.commit()
            return jsonify({"success": True, "result": actor.format(), "timestamp": time.time()}), 201
        except BadRequestException as err:
            abort(400)
        except AuthError:
            abort(401)
        except Exception as err:
            db.session.rollback()
            return jsonify({"success": False}), 500
        finally:
            db.session.close()

    @app.route('/agents', methods=["POST"])
    @requires_auth('post:agents')
    def create_new_agent():
        '''
        Create a new Agent
        ---
        tags:
          - Agents
        parameters:
          - name: Agent
            in: body
            schema:
              type: object
              properties:
                name:
                    type: string
                email:
                    type: string
                phone_number:
                    type: string

        responses:
          201:
            description: Returns the new Agent
        '''
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
        except AuthError:
            abort(401)
        except Exception as err:
            db.session.rollback()
            return jsonify({"success": False, "error": str(err)}), 500
        finally:
            db.session.close()

    @app.route('/movies', methods=["POST"])
    @requires_auth('post:movies')
    def create_new_movie():
        '''
        Create a new Movie
        ---
        tags:
          - Movies
        parameters:
          - name: Movie
            in: body
            schema:
              type: object
              properties:
                title:
                    type: string
                release_date:
                    type: date
                synopsis:
                    type: string
                rating:
                    type: number

        responses:
          201:
            description: Returns the new Movie
        '''
        try:
            body = request.get_json()

            if body is None:
                abort(400)

            user_input = {
                "title": body.get('title', None),
                "release_date": body.get('release_date', None),
                "synopsis": body.get('synopsis', None),
                "rating": body.get('rating', None),
            }
            movie = Movie(
                title=user_input['title'], release_date=user_input['release_date'], synopsis=user_input['synopsis'], rating=user_input['rating'])

            db.session.add(movie)
            db.session.commit()
            return jsonify({"success": True, "result": movie.format(), "timestamp": time.time()}), 201
        except AuthError:
            abort(401)
        except Exception as err:
            db.session.rollback()
            return jsonify({"success": False, "error": str(err)}), 500
        finally:
            db.session.close()

    @app.route('/actors/<int:id>', methods=["PATCH"])
    @requires_auth('patch:actors')
    def update_actor(id):
        '''
        Update an existing Actor
        ---
        tags:
          - Actors
        parameters:
          - name: id
            in: path
            type: number
          - name: Actor
            in: body
            schema:
              type: object
              properties:
                name:
                    type: string
                age:
                    type: number
                gender:
                    type: string
                headshot_url:
                    type: string
                agent_id:
                    type: number
                movies:
                    type: array
                    items:
                        type: number
        responses:
          200:
            description: Returns the updated Actor
        '''
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

            db.session.commit()

            return jsonify({"success": True, "result": actor.format(), "timestamp": time.time()}), 200
        except AuthError:
            abort(401)
        except Exception as err:
            db.session.rollback()
            return jsonify({"success": False, "error": str(err)}), 500

        finally:
            db.session.close()

    @app.route('/agents/<int:id>', methods=["PATCH"])
    @requires_auth('patch:agents')
    def update_agent(id):
        '''
        Update an existing Agent
        ---
        tags:
          - Agents
        parameters:
          - name: id
            in: path
            type: number
          - name: Agent
            in: body
            schema:
              type: object
              properties:
                name:
                    type: string
                email:
                    type: string
                phone_number:
                    type: string

        responses:
          200:
            description: Returns the updated Agent
        '''
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

            db.session.commit()

            return jsonify({"success": True, "result": agent.format(), "timestamp": time.time()}), 200
        except AuthError:
            abort(401)
        except Exception as err:
            db.session.rollback()
            return jsonify({"success": False, "error": str(err)}), 500

        finally:
            db.session.close()

    @app.route('/movies/<int:id>', methods=["PATCH"])
    @requires_auth('patch:movies')
    def update_movie(id):
        '''
        Update an existing Movie
        ---
        tags:
          - Movies
        parameters:
          - name: id
            in: path
            type: number
          - name: Movie
            in: body
            schema:
              type: object
              properties:
                title:
                    type: string
                release_date:
                    type: date
                synopsis:
                    type: string
                rating:
                    type: number

        responses:
          200:
            description: Returns the updated Movie
        '''
        try:
            body = request.get_json()

            if body is None:
                abort(400)

            movie = Movie.query.filter(Movie.id == id).first()

            if movie is None:
                abort(400)

            user_input = {
                "title": body.get('title', movie.title),
                "release_date": body.get('release_date', movie.release_date),
                "synopsis": body.get('synopsis', movie.synopsis),
                "rating": body.get('rating', movie.rating),
            }

            movie.title = user_input['title']
            movie.release_date = user_input['release_date']
            movie.synopsis = user_input['synopsis']
            movie.rating = user_input['rating']

            db.session.commit()

            return jsonify({"success": True, "result": movie.format(), "timestamp": time.time()}), 200
        except AuthError:
            abort(401)
        except Exception as err:
            db.session.rollback()
            return jsonify({"success": False, "error": str(err)}), 500

        finally:
            db.session.close()

    @app.route('/actors/<int:id>', methods=["DELETE"])
    @requires_auth('delete:actors')
    def delete_actor(id):
        '''
        Delete an Actor
        ---
        tags:
          - Actors
        parameters:
          - name: id
            in: path
            type: number
        responses:
          200:
            description: Returns successful
        '''
        try:
            actor = Actor.query.filter(Actor.id == id).first()
            if actor is None:
                raise BadRequestException('No actor found with ID %i' % (id))
            actor.delete()
            return jsonify({"success": True, "timestamp": time.time()}), 200
        except AuthError:
            abort(401)
        except BadRequestException as err:
            db.session.rollback()
            abort(400, err)
        except Exception as err:
            db.session.rollback()
            abort(500)
        finally:
            db.session.close()

    @app.route('/agents/<int:id>', methods=["DELETE"])
    @requires_auth('delete:agents')
    def delete_agent(id):
        '''
        Delete an Agent
        ---
        tags:
          - Agents
        parameters:
          - name: id
            in: path
            type: number
        responses:
          200:
            description: Returns successful
        '''
        try:
            agent = Agent.query.filter(Agent.id == id).first()
            if agent is None:
                raise BadRequestException()
            agent.delete()
            return jsonify({"success": True, "timestamp": time.time()}), 200
        except AuthError:
            abort(401)
        except BadRequestException:
            db.session.rollback()
            abort(400)
        except Exception as err:
            db.session.rollback()
            abort(500)
        finally:
            db.session.close()

    @app.route('/movies/<int:id>', methods=["DELETE"])
    @requires_auth('delete:movies')
    def delete_movie(id):
        '''
        Delete a Movie
        ---
        tags:
          - Movies
        parameters:
          - name: id
            in: path
            type: number
        responses:
          200:
            description: Returns successful
        '''
        try:
            movie = Movie.query.filter(Movie.id == id).first()
            if movie is None:
                raise BadRequestException()
            movie.delete()
            return jsonify({"success": True, "timestamp": time.time()}), 200
        except AuthError:
            abort(401)
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

    @app.errorhandler(AuthError)
    def user_is_unauthenticated(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "User not authenticated"
        }), 401
    return app


app = create_app()

if __name__ == '__main__':
    app.run()
