from src.portfolio import Portfolio
from src.rest import RestQueries
import json


pf = Portfolio()

ourpf = pf.getportfolio(1830)
with open('portfolio.txt', 'w') as outfile:
    json.dump(ourpf, outfile, indent=4)

pfref = pf.getportfolio(2201)
with open('ref.txt', 'w') as outfile:
    json.dump(pfref, outfile, indent=4)

ratio = RestQueries.get("ratio")
with open('ratio.txt', 'w') as outfile:
    json.dump(ratio, outfile, indent=4)

body = {"ratio": [12], "asset": [1860, 1900], "start_date": "2012-01-02", "end_date": "2020-11-24"}
sharpes = RestQueries.post('ratio/invoke', body)
with open('sharpelist.txt', 'w') as outfile:
    json.dump(sharpes, outfile, indent=4)
