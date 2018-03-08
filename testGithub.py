import unittest


class TestUser(unittest.TestCase):

    def test_user(self):

        self.assertEqual(parse_user('xli119567'), {'GithubApi567': 16, 'Triangle567': 5})

