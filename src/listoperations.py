from src.myasset import Asset


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