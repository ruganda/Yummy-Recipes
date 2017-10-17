from unittest import TestCase
from users import Users

class TestUsers(TestCase):
    """This class will handle all the functions to test for the user entry functions"""

    def setUp(self):
        """This method defines the test fixture for all test to be undertaken"""
        self.new_user = Users()

    def test_register_user(self):
        """This will the function user_register"""
        result = self.new_user.register_user("kaguna", "kaguna@gmail.com", "password", "password")
        self.assertEqual(2,result,"User registration successful")

