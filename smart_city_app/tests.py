from django.test import TestCase
from smart_city_app.functions import *

# Create your tests here.
class functions_tests(TestCase):

    def test_get_user_by_id(self):
        user = get_user_by_id(1)
        self.Equal(user.username, "admin")