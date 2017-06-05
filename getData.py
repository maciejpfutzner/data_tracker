from googlefinance import getQuotes
import json
import datetime
from pytz import timezone

#-------------------------------------------------------#

def getInfo(Stock):
    fetchedData = getQuotes(Stock)
    return fetchedData[0]

def getSpecific(Stock, Info):
    fetchedData = getQuotes(Stock)
    return fetchedData[0][Info]

def getPrice():
    return getSpecific(Stock, "LastTradePrice")

def isOpen(TradeTime):

    Year, Month, Day, Hour, Minute, Second = int(TradeTime[0:4]), int(TradeTime[5:7]), int(TradeTime[8:10]), int(TradeTime[11:13]),int(TradeTime[14:16]), int(TradeTime[17:19])

    tz = timezone('US/Eastern')
    now = datetime.datetime.now(tz)

    stockTime = now.replace(hour=Hour, minute=Minute, second=Second, microsecond=0)
    openTime = now.replace(hour=9, minute=30, second=0, microsecond=0)
    closeTime = now.replace(hour=16, minute=00, second=0, microsecond=0)

    if (stockTime > openTime) and (stockTime < closeTime):
        print "Stock is currently trading."
        return True

    else:
        print "Stock is no longer trading."
        return False

#-------------------------------------------------------#
if __name__ == '__main__':


    Stock = "BARC"


    #Price =  float(getInfo(Stock, "LastTradePrice"))
    #TradeTime = getInfo(Stock, "LastTradeDateTime")


    print getInfo(Stock)
    print getPrice()





