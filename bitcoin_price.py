import requests

API = "http://api.coindesk.com/v1/bpi/currentprice.json"

last_price = 0
# TODO: Try to catch timeout exceptions?...
def get_bpi_info():
    try:
        req = requests.get(API, timeout=5)
        if req.status_code == 200:
            return req.json()
        else:
            return {"bpi":{"USD": {"rate_float": str(last_price)}}}
    except requests.exceptions.ReadTimeout:
        return {"bpi":{"USD": {"rate_float": str(last_price)}}}


# Get Bitcoin rate in currency
def get_rate(currency="usd"):
    currency = currency.upper()
    bpi_info = get_bpi_info()
    global last_price
    last_price = bpi_info['bpi'][currency]["rate_float"]
    return last_price


if __name__ == '__main__':
    print "Current Bitcoin Price Index rate is %g USD" % get_rate()
    print "\tPowered by CoinDesk"
