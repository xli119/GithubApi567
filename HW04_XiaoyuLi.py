"""
@author: Xiaoyu Li
Created on 2/13/2018

"""
import json
import requests
import unittest


class TestUser(unittest.TestCase):
    def test_user(self):
        self.assertEqual(parse_user('xli119567'), {'GithubApi567': 12, 'Triangle567': 5})


def parse_user(id):
    r = requests.get('https://api.github.com/users/' + id + '/repos')
    print('User: ', id)
    results = dict()
    for repo in r.json():
        c = requests.get('https://api.github.com/repos/'+ id + '/' + repo['name'] + '/commits')
        print('Repo: ', repo['name'], 'Number of Commits:', len(c.json()))
        results[repo['name']] = len(c.json())
    return results

def main():
    user = input('Please enter an user id:')
    parse_user(user)

if __name__ == '__main__':

    unittest.main()


