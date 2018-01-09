from flask import Flask, render_template
import jinja2
import requests
import json
import datetime as dt

class Stock:

    def __init__(self):
        return 

def fetchData(url):
    try:
        raw_data = requests.get(url,timeout=10)
        data = json.loads(raw_data.text) # JSON Data
    except TimeoutError as err:
        print(err)
        data = {"status": "error"} #Err Code
    return data

def share():
    try:
        quote  = request
        basicQuote = quote["basicQuote"]
        stockName = basicQuote["name"]
        primaryExchange = basicQuote["primaryExchange"]
        currentPrice = basicQuote["price"]
        priceChange1Day = basicQuote["priceChange1Day"]
        percentChange1Day = basicQuote["percentChange1Day"]
        priceDate = basicQuote["priceDate"]
        lastUpdateTime = basicQuote["lastUpdateTime"]
        userTimeZone = basicQuote["userTimeZone"]

        print("Name: ",stockName)
        print("Primary Exchange: ",primaryExchange)
        print("Current Price: ",currentPrice)
        print("Price Change Today: ",priceChange1Day)
        print("Percent Change Today: ",percentChange1Day)
        print("Date of Price: ",priceDate)
        print("Last Update: ",lastUpdateTime)
        print("Timezone: ",userTimeZone)

    except TimeoutError as err:
        print("Program Timed Out Please Try again, or insure that you are connected to a network")
        data = {"status":"error"}
        return data


def priceTimeShare():
    try:    
        quote = request
        priceTimeSeries = quote["priceTimeSeries"]
        price = [priceTimeSeries[0]["price"] for var in priceTimeSeries]
        for val in price:
            for price in val:
                print(price)

    except TimeoutError as err:
        print("Program Timed Out Please Try again, or insure that you are connected to a network")
        data = {"status":"error"}
        return data


        

try:
    symbol = input("Input a Valid Stock Symbol: ")
    request = fetchData('https://www.bloomberg.com/markets/api/quote-page/'+ symbol +'%3AUS?locale=en')
    share()
    print(" \n Chart Data: \n")
    priceTimeShare()

except TimeoutError as err: 
    print("Program Timed Out Please Try again, or insure that you are connected to a network")
    data = {"status":"error"}
    print(data)

except KeyError as err:
    print("Program Timed Out Please Try again, or insure that you are connected to a network")
    data = {"status":"error"}
    print(data)

