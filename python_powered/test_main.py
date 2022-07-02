import unittest
import unittest.mock


import main


class TestHello(unittest.TestCase):
    def test_hello_name_with_name(self):
        name = "test"
        req = unittest.mock.Mock(args={"food": "pizza"})

        # Call tested function
        assert main.get_food(req) == "Hello {}!".format(name)
