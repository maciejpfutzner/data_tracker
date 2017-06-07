# StockBit - display stock exchange or Bitcoin prices in real time!

Challenge \#12 at the UCL PPC Hackathon - Team 7

Current stock exchange price of a chosen company or the bitcoin rate is displayed on a 4-digit 7-segment LED display, driven by an Arduino (actually a DCcduino), connected serially to a PC/Mac with a python app getting the data from the Web.

Stock exchange prices come from the [googlefinance](https://github.com/hongtaocai/googlefinance) module and the Bitcoin Price Index is provided by the [CoinDesk API](http://www.coindesk.com/price/).

![Picture of the setup](https://github.com/maciejpfutzner/data_tracker/blob/master/photo.jpg)


### How to install missing packages

`pip install -r requirements.txt`

We need the latest dev version of `googlefinance`, follow instructions [from here](https://github.com/hongtaocai/googlefinance) to install it from a git clone (clone it somewhere outside the data\_tracker dir)
