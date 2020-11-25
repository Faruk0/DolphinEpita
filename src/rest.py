import requests
import json


class RestQueries:
    base_uri = "https://dolphin.jump-technology.com:8443/api/v1/"
    group_id = 1830
    creds = {}
    with open("credentials.json", "r") as fd:
        creds = json.loads(fd.read())
    if len(creds) == 0:
        raise ("Error:credentials.json could not be parsed")

    def get(path):
        res = requests.get(RestQueries.base_uri + path,
                           auth=requests.auth.HTTPBasicAuth(
                               RestQueries.creds['username'],
                               RestQueries.creds['password']))
        return res.json()

    def post(path, content):
        res = requests.post(RestQueries.base_uri + path,
                            data=content,
                            auth=requests.auth.HTTPBasicAuth(RestQueries.creds['username'],
                                                             RestQueries.creds['password']))
        return res.json()

    def put(path, content):
        res = requests.put(RestQueries.base_uri + path,
                           data=content,
                           auth=requests.auth.HTTPBasicAuth(RestQueries.creds['username'],
                                                            RestQueries.creds['password']))
        return res
