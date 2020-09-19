import requests
import json
import argparse
import pandas as pd
from pandas_datareader import data as pdr
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl import load_workbook
from matplotlib import pyplot as plt
import time

class Nasdaq(object):

    def __init__(self, ticker, assetClass):

        self.__ticker = ticker
        self.__assetClass = assetClass

    def getStockInfo(self, ticker):
        url = "https://api.nasdaq.com/api/quote/{}/info?assetclass={}".format(self.__ticker, self.__assetClass)
        req = self.getDataFromURL(url)
        return req


    def getSummaryInfo(self, ticker):
        url = "https://api.nasdaq.com/api/quote/{}/summary?assetclass={}".format(self.__ticker, self.__assetClass)
        req = self.getDataFromURL(url)
        return req

    def chartInfo(self, ticker):
        url = "https://api.nasdaq.com/api/quote/{}/chart?assetclass={}".format(self.__ticker, self.__assetClass)
        req = self.getDataFromURL(url)
        return req

    def getCompanyInfo(self, ticker):
        url = "https://api.nasdaq.com/api/company/{}/company-profile".format(self.__ticker, self.__assetClass)
        req = self.getDataFromURL(url)
        return req

    def getDataFromURL(self, url):
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Host": "api.nasdaq.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0"
        }
        r = requests.get(url, headers=headers, timeout=5)
        print(r.url)
        json_data = r.json()
        # with open('summary-copy.json','w') as fp:
        #     json.dump(json_data, fp, indent = 4, ensure_ascii=False) # dumps to json file.
        return json_data
        # df = pd.DataFrame(json_data)
        # print(df)
        # return df

    def getMarketStatus(self):
        url = "https://api.nasdaq.com/api/market-info"
        info = self.getDataFromURL(url)
        marketIndicator = info["data"]["marketIndicator"]
        marketOpen = info["data"]["marketOpeningTime"]
        marketClose = info["data"]["marketClosingTime"]
        if marketIndicator == "Market Closed":
            return "The market is closed and will reopen on {}".format(marketOpen)
        else:
            return "The market is currently opened and will close at {}".format(marketClose)


    def getChartDetails(self):
        info = self.chartInfo()
        chartData = info['data']['chart']
        rev_data = chartData[::-1]
        chart_df = pd.json_normalize(rev_data)
        ax = chart_df.plot(lw=2, colormap='jet', marker='', markersize=10,
                           title=info["data"]["symbol"], x="z.dateTime", y="y")
        ax.set_xlabel("Date")
        ax.set_ylabel("Price in USD")
        plt.show()


    def getFullInfo(self, ticker):
        info = self.getStockInfo(ticker)
        time.sleep(3)
        summary = self.getSummaryInfo(ticker)

        # print(info)
        # print(summary)

        fullData = {"info": {}, "summary": {}}
        fullData["info"].update(info)
        fullData["summary"].update(summary)

        # print(fullData)

        return fullData

        # with open('out6.json', 'w') as fp:
        #     json.dump(fullData, fp, indent=4, ensure_ascii=False)  # dumps to json file.

    # def getBatchStockInfo(self):
    #     url = "https://api.nasdaq.com/api/quote/{}/info?assetclass={}".format(self.__ticker, self.__assetClass)
    #     # req = self.getBatchDataFromURL(url)
    #     return url

    # def getBatchDataFromURL(self, links):
    #     headers = {
    #         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    #         "Accept-Encoding": "gzip, deflate, br",
    #         "Accept-Language": "en-US,en;q=0.5",
    #         "Connection": "keep-alive",
    #         "Host": "api.nasdaq.com",
    #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0"
    #     }
    #     for url in links:
    #         r = requests.get(url, headers=headers, timeout=5)
    #         print(r.url)
    #         json_data = r.json()
    #         df = pd.DataFrame(json_data)

