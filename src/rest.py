import requests
import json

class RestQueries:

    base_uri = "https://dolphin.jump-technology.com:8443/api/v1/"

    creds = {}
    with open("credentials.json", "r") as fd:
        creds = json.loads(fd.read())
    if len(creds) == 0:
        raise("Error:credentials.json could not be parsed")

    def get(self, path):
        res = requests.get(RestQueries.base_uri + path,
                           auth=requests.auth.HTTPBasicAuth(
                               RestQueries.creds['username'],
                               RestQueries.creds['password']))
        return res.json()

    def post(self, path, content):
        res = requests.get(base_uri + path,
                           data=content,
                           auth=requests.auth.HTTPBasicAuth(creds['username'],
                                                            creds['password']))
        return res.json()

    def post(self, path, content):
        res = requests.get(base_uri + path,
                           data=content,
                           auth=requests.auth.HTTPBasicAuth(creds['username'],
                                                            creds['password']))
        return res.json()
