import json

# Choose either "Bitcoin" or "Stock"
Type = "Stock"
# Choose stock (code name)
StockName = "BARC"
# Upper threshold limit (percentage)
ULim = 0.5
# Lower threhold limit (percentage)
LLim = 0.5

#-------------------------------------------------------#
if __name__ == '__main__':

    setup = {'Type':Type, 'Stock':StockName, 'UpperLimit':ULim, 'LowerLimit':LLim}


    with open('setupfile.txt', 'w') as outfile:
        json.dump(setup, outfile)
