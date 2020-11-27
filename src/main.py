import argparse
import json

from rest import RestQueries
from myasset import Asset
from currencies import Currencies
from portfolio import Portfolio

def create_assets(jsonAssets):
    assets = []
    for asset in jsonAssets:
        if asset["TYPE"]["value"] != "STOCK":
            continue
        if not "LAST_CLOSE_VALUE" in asset:
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
            asset.sharpe = float(sharpeDict[str(asset.id)]["12"]["value"].replace(",", "."))
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

def computeQty(portfolio):
    for asset in portfolio.items:
        totVal = portfolio.value * asset.sharpe / portfolio.totSharpe
        asset.qty = int(1000 * totVal / portfolio.value)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Dolphin project")

    parser.add_argument("-S", "--sharpe",
                        required=False, help="Load sharpe values from file")
    parser.add_argument("-A", "--assets",
                        required=False, help="Load assets values from file")
    parser.add_argument("-oS", "--output-sharpe",
                        required=False, help="Dump sharpe values to file")
    parser.add_argument("-oA", "--output-assets",
                        required=False, help="Dump assets values to file")
    args = parser.parse_args()

    responseAssets = None
    if args.assets is not None:
        with open(args.assets, "r") as fd:
            responseAssets = json.loads(fd.read())
    else:
        responseAssets = RestQueries.get("asset?columns=ASSET_DATABASE_ID&columns=LABEL&columns=LAST_CLOSE_VALUE&columns=TYPE&date=2016-06-01")

    if args.output_assets is not None:
        with open(args.output_assets, "w") as fd:
            fd.write(json.dumps(responseAssets, indent=4))

    assets = create_assets(responseAssets)

    sharpeDict = None
    if args.sharpe is not None:
        with open(args.sharpe, "r") as fd:
            sharpeDict = json.loads(fd.read())
    else:
        sharpeDict = get_all_sharpe(assets)

    if args.output_sharpe is not None:
        with open(args.output_sharpe, "w") as fd:
            fd.write(json.dumps(sharpeDict, indent=4))

    load_sharpes(assets, sharpeDict)

    bestassets = computelist(assets)

    portfolio = Portfolio()

    for asset in bestassets:
        portfolio.additem(asset)

    computeQty(portfolio)

    res = portfolio.putPortfolio()
    lowerNavs, greaterNavs = portfolio.checkNav()
    while len(lowerNavs) > 0 or len(greaterNavs) > 0:
        for asset in lowerNavs:
            asset.qty = asset.qty + asset.sharpe
        for asset in greaterNavs:
            asset.qty = asset.qty - asset.sharpe
        lowerNavs, greaterNavs = portfolio.checkNav()
        print(len(lowerNavs), len(greaterNavs), len(lowerNavs) + len(greaterNavs))
    print("OK")
    print(portfolio.checkNav())
    res = portfolio.putPortfolio()
    res = RestQueries.get("portfolio/1830/dyn_amount_compo")
    print(json.dumps(res, indent = 4))
