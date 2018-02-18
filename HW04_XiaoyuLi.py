"""
@author: Xiaoyu Li
Created on 2/13/2018

"""
import json
import requests


def parse_user(id):
    r = requests.get('https://api.github.com/users/' + id + '/repos')
    print('User: ', id)
    for repo in r.json():
        c = requests.get('https://api.github.com/repos/'+ id + '/' + repo['name'] + '/commits')
        print('Repo: ', repo['name'], 'Number of Commits:', len(c.json()))

def main():
    user = input('Please enter an user id:')
    parse_user(user)

if __name__ == '__main__':
    main()


