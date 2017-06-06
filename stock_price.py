from googlefinance import getQuotes
import json
import datetime
import time
from pytz import timezone
import re

#-------------------------------------------------------#

Stock = "AAPL"

# Returns a string of stock information, including price, trade time etc
def getInfo(Stock):
    fetchedData = getQuotes(Stock)
    return fetchedData[0]

# Returns specific information on request
def getSpecific(Stock, Info):
    return getInfo(Stock)[Info]

# Returns price of stock
def getPrice(Stock):
    price = (getSpecific(Stock, "LastTradePrice")).replace(",", "")
    return price

# Returns trade time
def getTradeTime(Stock):
    print "Current time:", getSpecific(Stock, "LastTradeTime")
    return getSpecific(Stock, "LastTradeTime")

# Returns index (NASTAQ, LON etc)
def getIndex(Stock):
    return getSpecific(Stock, "Index")

def getOpenPrice(Stock):
    price = (getSpecific(Stock, "PreviousClosePrice")).replace(",", "")
    return price

# Checks if market is trading. Currently works for NASDAQ & LSE
def isOpen():
    Index = getIndex()
    TradeTime = getSpecific("LastTradeDateTime")
    Hour, Minute, Second = int(TradeTime[11:13]),int(TradeTime[14:16]), int(TradeTime[17:19])
    if (Index == "NASDAQ"):
        tz = timezone('US/Eastern')
        now = datetime.datetime.now(tz)
        stockTime = now.replace(hour=Hour, minute=Minute, second=Second, microsecond=0)
        openTime = now.replace(hour=9, minute=30, second=0, microsecond=0)
        closeTime = now.replace(hour=16, minute=00, second=0, microsecond=0)
    if (Index == "LON"):
        tz = timezone('US/Eastern')
        now = datetime.datetime.now(tz)
        stockTime = now.replace(hour=Hour, minute=Minute, second=Second, microsecond=0)
        openTime = now.replace(hour=8, minute=00, second=0, microsecond=0)
        closeTime = now.replace(hour=16, minute=30, second=0, microsecond=0)
    if (stockTime > openTime) and (stockTime < closeTime):
        print Index, "stock market is currently trading."
        return True
    else:
        print Index, "stock is no longer trading."
        return False

#-------------------------------------------------------#
if __name__ == '__main__':

    print getInfo(Stock)
    print getOpenPrice(Stock)







