import argparse
import json

from rest import RestQueries
from myasset import Asset
from currencies import Currencies


def create_assets(jsonAssets):
    assets = []
    for asset in jsonAssets:
        if asset["TYPE"]["value"] != "STOCK":
            continue
        val = float(asset["LAST_CLOSE_VALUE"]["value"].replace(",", ".").split(" ")[0])
        curName = asset["LAST_CLOSE_VALUE"]["value"].split(" ")[1]
        val *= Currencies.addOrGetCur(curName)

        assets.append(Asset(id = int(asset["ASSET_DATABASE_ID"]["value"]),  #id
                            name = asset["LABEL"]["value"],              #name
                            type = asset["TYPE"]["value"],               #type
                            value = val))
    return assets

def get_all_sharpe(assetList):
    ids = []
    ratio = [ 12 ]
    start_date = "2016-06-01"
    end_date = "2020-09-30"

    for asset in assetList:
        ids.append(asset.id)

    data = {
        "ratio" : ratio,
        "asset" : ids,
        "benchmark" : None,
        "start_date" : start_date,
        "end_date" : end_date,
        "frequency" : None
    }

    responseSharpe = RestQueries.post("ratio/invoke", json.dumps(data))
    return responseSharpe

def load_sharpes(assetList, sharpeDict):
    for asset in assetList:
        if str(asset.id) in sharpeDict:
            asset.sharpe = sharpeDict[str(asset.id)]["12"]["value"]
        else:
            print("ID {asset.id}: Not in sharpe list")

def findmin(assets):
    min = 0
    value = assets[0].sharpe
    for i in range(1, len(assets)):
        if value > assets[i].sharpe:
            min = i
            value = assets[i].sharpe
    return min

def computelist(assets):
    result = []
    for i in range(len(assets)):
        if len(result) < 20:
            result.append(assets[i])
            continue
        min = findmin(result)
        if assets[i].sharpe > result[min].sharpe:
            result[min] = assets[i]
    return result

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Dolphin project")

    parser.add_argument("-S", "--sharpe",
                        required=False, help="Load sharpe values from file")
    parser.add_argument("-A", "--assets",
                        required=False, help="Load assets values from file")
    args = parser.parse_args()

    responseAssets = None
    if args.assets is not None:
        with open(args.assets, "r") as fd:
            responseAssets = json.loads(fd.read())
    else:
        responseAssets = RestQueries.get("asset")

    assets = create_assets(responseAssets)

    sharpeDict = None
    if args.sharpe is not None:
        with open(args.sharpe, "r") as fd:
            sharpeDict = json.loads(fd.read())
    else:
        sharpeDict = get_all_sharpe(assets)

    load_sharpes(assets, sharpeDict)

    for i in assets:
        print(i.toString())

    bestassets = computelist(assets)
