import requests
import json
from ap import Nasdaq
import argparse
import pandas as pd

# if __name__=="__main__":

#   argparser = argparse.ArgumentParser()
#   argparser.add_argument('ticker',help = 'Ticker Symbol')
#   argparser.add_argument('assetclass',help = 'AssetClass')
#   args = argparser.parse_args()
#   ticker = args.ticker
#   assetclass = args.assetclass
#   api = Nasdaq(ticker, assetclass)
#   info = api.getFullInfo(ticker)
  
  # with open('out_info.json', 'w') as fp:
  #    json.dump(info, fp, indent=4, ensure_ascii=False)  # dumps to json file.

f = open("outputPretty.json")
obj = json.load(f)
# print(obj)


df = pd.DataFrame(obj)
df.drop(obj["pressReleases"])
print(df)