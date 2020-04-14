import os
import unittest
import json

from flask_sqlalchemy import SQLAlchemy

from models import setup_db
from app import create_app


class CastingTests(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = os.environ['DATABASE_URL']
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    ''' TEST CASE: [GET]/questions '''

    def test_root(self):
        res = self.client().get('/')
        self.assertEqual(res.status_code, 200)

    def test_get_actors(self):
        res = self.client().get('/actors')
        self.assertEqual(res.status_code, 200)

    def test_get_movies(self):
        res = self.client().get('/movies')
        self.assertEqual(res.status_code, 200)

    def test_get_agents(self):
        res = self.client().get('/agents')
        self.assertEqual(res.status_code, 200)

        # Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
