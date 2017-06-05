import stock_price as sp
import bitcoin_price as bp
import time
import json
import os
import arduino_comm as acomm


# Converts number to string and sorts formatting for arduino
def convertToString(number):
    number = round(float(number),1)
    decimal = str(4 - str(number).find("."))
    numStr = (str(number).replace(".", "")).zfill(4)
    numStr = "n" + numStr[0:4] + decimal
    return numStr


#-------------------------------------------------------#
if __name__ == '__main__':

    acomm.init()

    # Main loop to run the stockbit algorithm
    while True:
        with open('setupfile.txt') as json_file:
            setup = json.load(json_file)
    
        Type = str(setup["Type"])
        Stock = str(setup["Stock"])
        ULimit = float(setup["UpperLimit"])
        LLimit = float(setup["LowerLimit"])
        
        if Type == "Stock":
            
            print "Current stock:", Stock
            sp.getPrice(Stock)
            sp.getTradeTime(Stock)
            string = convertToString(sp.getPrice(Stock))
        
        elif Type == "Bitcoin":
        
            print "Current type:", Type
            print bp.get_rate()
            string = convertToString(bp.get_rate())
        
        acomm.send_command(string)
        #acomm.send_command("b")
        print " "
        
        
        
        
        time.sleep(5)
