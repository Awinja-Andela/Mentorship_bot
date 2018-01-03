import json
import unittest


from Mentorship_bot import create_app, query_string_1, query_string_2
from app.models import db


class BotApiTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.ctx = self.app.app_context()
        self.client = self.app.test_client()
        self.ctx.push()
        db.drop_all()
        db.create_all()

    def test_register_mentor(self):
        resp = self.client.post('/bot',
                                data=json.dumps(query_string_1),
                                content_type="application/json")
        self.assertEqual(resp.status_code, 200)
        result = json.loads(resp.data)
        self.assertEqual(result['message'],
                         "Thank you for availing yourself as a mentor.")

    def test_replicate_mentor(self):
        resp = self.client.post('/bot',
                                data=json.dumps(query_string_1),
                                content_type="application/json")
        self.assertEqual(resp.status_code, 200)
        resp_1 = self.client.post('/bot',
                                  data=json.dumps(query_string_1),
                                  content_type="application/json")
        self.assertEqual(resp_1.status_code, 201)

    def test_get_mentors_in_stack(self):
        resp = self.client.post('/bot',
                                data=json.dumps(query_string_1),
                                content_type="application")
        self.assertEqual(resp.status_code, 200)
        resp_1 = self.client.post('/bot',
                                  data=json.dumps(query_string_2),
                                  content_type="application/json")
        self.assertEqual(resp_1.status_code, 200)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.context.pop()


if __name__ == '__main__':
    unittest.main()
