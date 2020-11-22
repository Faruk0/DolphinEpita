import requests
import json

if __name__ == "__main__":
    base_uri = "https://dolphin.jump-technology.com:8443/api/v1/"

    with open("credentials.json", "r") as fd:
        creds = json.loads(fd.read())

    response = requests.get(base_uri + "asset",
                            auth=requests.auth.HTTPBasicAuth(creds['username'],
                                                             creds['password']))
    print(response.text)
