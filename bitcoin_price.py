import requests

API = "http://api.coindesk.com/v1/bpi/currentprice.json"

# TODO: Try to catch timeout exceptions?...
def get_bpi_info():
    while True:
        req = requests.get(API)
        if req.status_code == 200:
            return req.json()

# Get Bitcoin rate in currency
def get_rate(currency="usd"):
    currency = currency.upper()
    bpi_info = get_bpi_info()
    return bpi_info['bpi'][currency]["rate_float"]


if __name__ == '__main__':
    print "Current Bitcoin Price Index rate is %g USD" % get_rate()
    print "\tPowered by CoinDesk"
