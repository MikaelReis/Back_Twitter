from django.test import TestCase
from users.factories import UsersFactory


class TestUserModel(TestCase):
    def setUp(self):
        self.user = UsersFactory(username="mikael", password="ebac")

    def test_user_created(self):
        self.assertEqual(self.user.username, "mikael")
        self.assertTrue(self.user.check_password("ebac"))
        self.assertIsNotNone(self.user.pk) 