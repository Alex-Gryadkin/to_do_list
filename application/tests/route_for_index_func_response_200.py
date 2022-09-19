import unittest
from application import app


class TestIndexRoute(unittest.TestCase):
    def test_index_route_WHEN_slash_THEN_response_200(self):
        # GIVEN
        route = '/'

        # WHEN
        with app.test_client() as c:
            response = c.get(route)

        # THEN
            self.assertEqual(response.status_code, 200)
