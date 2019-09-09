import json
import requests

# api_url_base = "https://interns.bcgdvsydney.com"
# r = requests.get(api_url_base + "/api/v1/key")
# content = r.json()
# print(r.status_code)
#
# key = content.get("key")
# print(key)
# contact = {"name": "Jianwen (Simon) Yang", "email": "jianwen.yeung@gmail.com"}
# payload = {"apiKey": key}
# r = requests.post(api_url_base + "/api/v1/submit", params=payload, data=json.dumps(contact))
# print(r.json())
#

class Submission:
    def __init__(self, name = '', email = ''):
        self._name = name
        self._email = email
        self._key = ''

    @property
    def name(self):
        return self.name

    @property
    def email(self):
        return self.email

    @name.setter
    def name(self, name):
        self._name = name

    @email.setter
    def email(self, email):
        self._email = email

    # function to retrieve api key from the given endpoint
    def get_api(self, url):
        '''
        :param url: endpoint url
        :return: http status code
        '''
        r = requests.get(url)
        content = r.json()
        self._key = content.get("key")
        print(r.status_code)
        return r.status_code

    # def post(self, url):
    #     contact = {"name": self._name, "email": self._email}
    #     payload = {"apiKey": self._key}
    #     r = requests.post(url, params=payload, data=json.dumps(contact))
    #     print(r.json())



