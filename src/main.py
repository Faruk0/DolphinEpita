import json
from rest import RestQueries
from myasset import Asset
from currencies import Currencies


def create_assets(jsonAssets):
    assets = []
    for asset in jsonAssets:
        val = float(asset["LAST_CLOSE_VALUE"]["value"].replace(",", ".").split(" ")[0])
        curName = asset["LAST_CLOSE_VALUE"]["value"].split(" ")[1]
        val *= Currencies.addOrGetCur(curName)

        assets.append(Asset(id = int(asset["ASSET_DATABASE_ID"]["value"]),  #id
                            name = asset["LABEL"]["value"],              #name
                            type = asset["TYPE"]["value"],               #type
                            value = val))
    return assets



if __name__ == "__main__":

    responseAssets = RestQueries.get("asset")
    assets = create_assets(responseAssets)
    for i in assets:
        print(i.toString())
    Currencies.dump()
