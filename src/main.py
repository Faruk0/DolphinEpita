import json
from rest import RestQueries
from myasset import Asset

def create_assets(jsonAssets):
    assets = []
    for asset in jsonAssets:
        val = float(asset["LAST_GROSS_VALUE"]["value"].replace(",", ".").split(" ")[0])
        assets.append(Asset(int(asset["ASSET_DATABASE_ID"]["value"]),  #id
                            asset["LABEL"]["value"],              #name
                            asset["TYPE"]["value"],               #type
                            0,                           #quantity
                            val,
                            0,                           #amount
                            0))                           #nav
    return assets
if __name__ == "__main__":

    responseAssets = RestQueries.get("asset")
    print(json.dumps(responseAssets[2], indent=4), type(responseAssets[2]))
    assets = create_assets(responseAssets)
    for i in assets:
        print(i.tostring())
