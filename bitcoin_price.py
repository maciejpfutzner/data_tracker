import requests
import json

API = "http://api.coindesk.com/v1/bpi/currentprice.json"

def get_bpi_info():
    return json.loads(requests.get(API).text)

def get_rate(currency="usd"):
    currency = currency.upper()
    bpi_info = get_bpi_info()
    return bpi_info['bpi'][currency]["rate_float"]


if __name__ == '__main__':
    print "Current Bitcoin Price Index rate is %g USD" % get_rate()
    print "\tPowered by CoinDesk"
