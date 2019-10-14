# 模拟登陆并爬取GitHub
import requests
from lxml import etree


class LoginGitHub(object):
    def __init__(self):
        self.headers = {
            'Referer': 'https://github.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'Host': 'github.com'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.logined_url = 'https://github.com/settings/profile'
        self.session = requests.Session()


def token(self):
    r = self.session.get(url=self.login_url, headers=self.headers)
    selector = etree.HTML(r.text)
    take = selector.xpath('//div//input[2]/@value')[0]
    return take


def login(self, email, password):
    post_data = {
        'commit': 'Sign in',
        'utf-8': '✓',
        'authenticity_token': self.token(),
        'login': email,
        'password': password
    }
    r = self.session.post(url=self.post_url, data=post_data, headers=self.headers)
    if r.status_code == 200:
        self.dynamics(r.text)
    r = self.session.get(url=self.login_url, headers=self.headers)
    if r.status_code == 200:
        self.profile(r.text)



