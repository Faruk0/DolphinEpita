import json
from rest import RestQueries

if __name__ == "__main__":

    tmp = RestQueries.get("asset")
    assets = json.loads(tmp)
    print(type(assets), assets[0], type(assets[0]))
