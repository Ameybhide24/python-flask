import hello_world
import unittest

class TestHelloWorld(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setUp(self):
        self.app = hello_world.app.test_client()
        self.app.testing = True

    @pytest.fixture(autouse=True)
    def test_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
    
    @pytest.fixture(autouse=True)
    def test_greeting_message(self):
        greeting = 'Welcome to CI/CD'
        self.assertEqual(hello_world.greet(), greeting)

if __name__ == '__main__':
    unittest.main()