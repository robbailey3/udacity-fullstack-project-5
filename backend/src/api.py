import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS
from flask_swagger import swagger
from models.models import db_drop_and_create_all, setup_db, db
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
        return jsonify({"timestamp": time.time(), "result": swag})

    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
