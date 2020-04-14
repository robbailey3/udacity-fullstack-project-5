import os
import unittest
import json

from flask_sqlalchemy import SQLAlchemy
from models import setup_db, db_drop_and_create_all
from app import create_app
import requests


# Ideally, this wouldn't have usernames and passwords in here. Because that's bad. Very bad.
users = {
    'rob.bailey3+casting-assistant@gmail.com': 'Password-1',
    'rob.bailey3+casting-director@gmail.com': 'Password-1',
    'rob.bailey3+executive-producer@gmail.com': 'Password-1',
}


class CastingTests(unittest.TestCase):

    def getUserToken(self, userName):
        url = 'https://fsnd-capstone.eu.auth0.com/oauth/token'
        headers = {'content-type': 'application/json'}

        password = users[userName]
        parameter = {"client_id": "E4VCDqiXdE5PNRag5E6NA6Mdcria1Qef",
                     "client_secret": "sxAQVr4LtKf_mIRcxDuG_vf0eu0Bu1uwOssNx-Zcb65ojrfA0xrXUX9xV3jrY5Ku",
                     "audience": 'FSND-Capstone-API',
                     "grant_type": "password",
                     "username": userName,
                     "password": password, "scope": "openid"}
        responseDICT = json.loads(requests.post(
            url, json=parameter, headers=headers).text)
        return responseDICT['access_token']

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
        """Executed after each test"""
        pass

    def test_root(self):
        res = self.client().get('/')
        self.assertEqual(res.status_code, 200)

    def test_add_movie(self):
        data = json.dumps({"title": "test title", "release_date": "10-10-2010",
                           "rating": 30, "synopsis": "Hello WOrld"})
        res = self.client().post('/movies',
                                 headers={'Authorization': "Bearer " + self.getUserToken("rob.bailey3+executive-producer@gmail.com"), "Content-Type": "application/json"}, data=data)
        self.assertEqual(res.status_code, 201)

    def test_add_movie_unauth(self):
        data = json.dumps({"title": "test title", "release_date": "10-10-2010",
                           "rating": 30, "synopsis": "Hello WOrld"})
        res = self.client().post('/movies',
                                 headers={"Content-Type": "application/json"}, data=data)
        self.assertEqual(res.status_code, 401)

    def test_add_agent(self):
        data = json.dumps({"name": "test agent", "phone_number": "12345678",
                           "email": "test@test.com"})
        res = self.client().post('/agents',
                                 headers={'Authorization': "Bearer " + self.getUserToken("rob.bailey3+executive-producer@gmail.com"), "Content-Type": "application/json"}, data=data)
        self.assertEqual(res.status_code, 201)

    def test_add_agent_unauth(self):
        data = json.dumps({"name": "test agent", "phone_number": "12345678",
                           "email": "test@test.com"})
        res = self.client().post('/agents',
                                 headers={"Content-Type": "application/json"}, data=data)
        self.assertEqual(res.status_code, 401)

    def test_add_actor(self):
        data = json.dumps({"name": "Bob", "age": "12",
                           "gender": "male", "headshot_url": "http://rureiewjhrewj"})
        res = self.client().post('/actors',
                                 headers={'Authorization': "Bearer " + self.getUserToken("rob.bailey3+executive-producer@gmail.com"), "Content-Type": "application/json"}, data=data)
        self.assertEqual(res.status_code, 201)
        data = json.loads(res.data)
        self.assertEqual(data['result']['name'], "Bob")

    def test_add_actor_2(self):
        data = json.dumps({"name": "Bob", "age": "12",
                           "gender": "male", "headshot_url": "http://rureiewjhrewj"})
        res = self.client().post('/actors',
                                 headers={'Authorization': "Bearer " + self.getUserToken("rob.bailey3+executive-producer@gmail.com"), "Content-Type": "application/json"}, data=data)
        self.assertEqual(res.status_code, 201)

    def test_add_actor_unauth(self):
        data = json.dumps({"name": "Bob", "age": "12",
                           "gender": "male"})
        res = self.client().post('/actors',
                                 headers={"Content-Type": "application/json"}, data=data)
        self.assertEqual(res.status_code, 401)

    def test_patch_actors_assistant(self):
        data = json.dumps({"name": "Bob"})
        res = self.client().patch(
            '/actors/1', headers={'Authorization': "Bearer " + self.getUserToken("rob.bailey3+casting-assistant@gmail.com")})
        self.assertEqual(res.status_code, 401)

    def test_patch_actors_director(self):
        id = json.loads(self.client().get('/actors', headers={'Authorization': "Bearer " + self.getUserToken(
            "rob.bailey3+executive-producer@gmail.com"), "Content-Type": "application/json"}).data)['result'][0]['id']
        data = json.dumps({"name": "Bob", "age": "12",
                           "gender": "male", "headshot_url": "http://url.com"})
        res = self.client().patch('/actors/' + str(id),
                                  headers={'Authorization': "Bearer " + self.getUserToken("rob.bailey3+casting-director@gmail.com"), "Content-Type": "application/json"}, data=data)
        self.assertEqual(res.status_code, 200)

    def test_patch_agents_assistant(self):
        data = json.dumps({"name": "Bob"})
        res = self.client().patch(
            '/agents/1', headers={'Authorization': "Bearer " + self.getUserToken("rob.bailey3+casting-assistant@gmail.com")})
        self.assertEqual(res.status_code, 401)

    def test_patch_agents_director(self):
        data = json.dumps({"name": "Bob", "age": "12",
                           "gender": "male", "headshot_url": "http://url.com"})
        res = self.client().patch('/agents/1',
                                  headers={'Authorization': "Bearer " + self.getUserToken("rob.bailey3+casting-director@gmail.com"), "Content-Type": "application/json"}, data=data)
        self.assertEqual(res.status_code, 200)

    def test_patch_agents_assistant(self):
        data = json.dumps({"title": "MOVIE_TITLE"})
        res = self.client().patch(
            '/movies/1', headers={'Authorization': "Bearer " + self.getUserToken("rob.bailey3+casting-assistant@gmail.com")})
        self.assertEqual(res.status_code, 401)

    def test_patch_agents_director(self):
        data = json.dumps({"title": "MOVIE_TITLE"})
        res = self.client().patch('/movies/1',
                                  headers={'Authorization': "Bearer " + self.getUserToken("rob.bailey3+casting-director@gmail.com"), "Content-Type": "application/json"}, data=data)
        self.assertEqual(res.status_code, 200)

    def test_delete_actors_unauth(self):
        res = self.client().delete('/actors/1')
        self.assertEqual(res.status_code, 401)

    def test_delete_actors(self):
        id = json.loads(self.client().get('/actors', headers={'Authorization': "Bearer " + self.getUserToken(
            "rob.bailey3+executive-producer@gmail.com"), "Content-Type": "application/json"}).data)['result'][0]['id']
        res = self.client().delete('/actors/' + str(id),
                                   headers={'Authorization': "Bearer " + self.getUserToken("rob.bailey3+executive-producer@gmail.com")})
        self.assertEqual(res.status_code, 200)

    def test_get_actors_unauth(self):
        res = self.client().get('/actors')
        self.assertEqual(res.status_code, 401)

    def test_get_movies_unauth(self):
        res = self.client().get('/movies')
        self.assertEqual(res.status_code, 401)

    def test_get_agents_unauth(self):
        res = self.client().get('/agents')
        self.assertEqual(res.status_code, 401)

    def test_get_actors_auth(self):
        res = self.client().get(
            '/actors', headers={'Authorization': "Bearer " + self.getUserToken("rob.bailey3+casting-assistant@gmail.com")})
        self.assertEqual(res.status_code, 200)

    def test_get_movies_auth(self):
        res = self.client().get(
            '/actors', headers={'Authorization': "Bearer " + self.getUserToken("rob.bailey3+casting-assistant@gmail.com")})
        self.assertEqual(res.status_code, 200)

    def test_get_agents_auth(self):
        res = self.client().get(
            '/actors', headers={'Authorization': "Bearer " + self.getUserToken("rob.bailey3+casting-assistant@gmail.com")})
        self.assertEqual(res.status_code, 200)

        # Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
