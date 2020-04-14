import os
import unittest
import json

from flask_sqlalchemy import SQLAlchemy

from models.models import setup_db
from api import create_app


class CastingTests(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.username = 'postgres'
        self.password = 'password'
        self.database_name = "capstone_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format(self.username, self.password,
                                                               'localhost:5432', self.database_name)
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

        # Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
