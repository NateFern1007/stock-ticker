# # pp dataDict
# type =  cfg["stockType"].keys
# symbol = cfg["stockType"].values


# req = Faraday.new('https://api.nasdaq.com/api/quote/AAPL/info?assetclass=stocks', headers: {
#     "Accept" => "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#     "Accept-Encoding" => "gzip, deflate, br",
#     "Accept-Language" => "en-US,en;q=0.5",
#     "Connection" => "keep-alive",
#     "Host" => "api.nasdaq.com",
#     "User-Agent" => "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0"
# }).get 

# pp req


# do `python url_grab.py xlk etfs` 


# loop do `python url_grab.py` sleep(15)

#     jsonData = JSON[open("out6.json"){ |file| file.read }]
#     infoData = jsonData["info"]["data"]
#     summaryData = jsonData["summary"]["data"]
#     infoDict = {
#         "companyName" => infoData["companyName"],
#         "primaryData" => infoData["primaryData"],
#         "summaryData" => summaryData["summaryData"].map{_2["value"]},

# }

# end 

# pp infoDict





# --header="Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8" --header="Accept-Language: en-US,en;q=0.5" --header="Accept-Encoding: gzip, deflate" --header="Connection: keep-alive --header="Upgrade-Insecure-Requests: 1" --header="DNT: 1" https://www.bloomberg.com/markets2/api/datastrip/%2CFNCL%3AUS%2CGILD%3AUS%2CHEDJ%3AUS%2CMGLN%3AUS%2CSPY%3AUS%2CV%3AUS%2CVV%3AUS%2CXLK%3AUS?locale=en&customTickerList=true -O dump.json` end


cfg = YAML.load_file("config.yaml")

stocks = cfg["Stocks"].join(",")

# dataDict = {
#     "mutualfunds" => cfg["stockType"]["MutualFunds"],
#     "etfs" => cfg["stockType"]["ExchangeTradedFunds"],
#     "stocks" => cfg["stockType"]["CommonStock"],

# }

# https://www.bloomberg.com/markets2/api/datastrip/FNCL:US,GILD:US,HEDJ:US,MGLN:US,SPY:US,V:US,VV:US,XLK:US?