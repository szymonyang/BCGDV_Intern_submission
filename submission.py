import json
import requests


class Submission:
    def __init__(self, name = '', email = ''):
        self._name = name
        self._email = email
        self._key = ''
        self._status_code = ''

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
        """
        :param url: endpoint url
        :return: http status code
        """
        url += "/api/v1/key"
        r = requests.get(url)
        content = r.json()
        self._key = content.get("key")
        self._status_code = r.status_code
        return r.status_code

    # function to submit details
    def post(self, url):
        """
        :param url: endpoint url
        :return: message of http response
        """
        if self._status_code != 201:
            print("Cannot get API key")
            return
        url += "/api/v1/submit"
        contact = {"name": self._name, "email": self._email}
        payload = {"apiKey": self._key}
        r = requests.post(url, params=payload, data=json.dumps(contact))
        if r.status_code == 202:
            return "{} Accepted".format(r.status_code)
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            # Need to check its an 404, 503, 500, 403 etc.
            print("error: ", e.response.status_code, " ", e.response.json().get("error"))


if __name__ == "__main__":
    fish = Submission("Salmon", "fish@gmail.com")
    status_code = fish.get_api("https://interns.bcgdvsydney.com")
    print(status_code)
    message = fish.post("https://interns.bcgdvsydney.com")
    print(message)


