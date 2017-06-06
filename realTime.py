import stock_price as sp
import bitcoin_price as bp
import time
import json
import os
import arduino_comm as acomm
import fakeData as fd
import setup


## Converts number to string and sorts formatting for arduino
def convertToString(number):
    number = round(float(number),1)
    decimal = str(4 - str(number).find("."))
    numStr = (str(number).replace(".", "")).zfill(4)
    numStr = "n" + numStr[0:4] + decimal
    return numStr


#-------------------------------------------------------#
if __name__ == '__main__':

    #acomm.init()

    ## Main loop to run the stockbit algorithm
    fakeIndex = 0
    while True:
        with open('setupfile.txt') as json_file:
            setup = json.load(json_file)

        Type = str(setup["Type"])
        Stock = str(setup["Stock"])
        ULim = float(setup["UpperLimit"])
        LLim = float(setup["LowerLimit"])
        Alarm = str(setup["Alarm"])
        
        
        if Type == "Stock":
            
            TradeTime = sp.getTradeTime(Stock)
            price = float(sp.getPrice(Stock))
            print Stock, "opening price:", price
            string = convertToString(sp.getPrice(Stock))
        
            if price < float(sp.getOpenPrice(Stock)):
                print "Price below opening"
                #acomm.send_command("or")
            if price > float(sp.getOpenPrice(Stock)):
                print "Price above opening"
                #acomm.send_command("og")
        
        elif Type == "Bitcoin":
        
            print "Current type:", Type
            print bp.get_rate()
            price = float(bp.get_rate())
            string = convertToString(bp.get_rate())
        
        elif Type == "Fake":
            print "Current type:", Type
            print fd.get_value(fakeIndex)

            fakeIndex = fakeIndex + 1
            if (fakeIndex >= len(fd.myArrayOfData)):
                fakeIndex = 0
            price = fd.get_value(fakeIndex)
            string = convertToString(fd.get_value(fakeIndex))

        #acomm.send_command(string)

        ## Checks lower limit and if statement is true turns on red LED and alarm
        if price < LLim and Alarm == "on":
            print "Alarm on for lower limit"
            #acomm.send_command("ora")
            setup.setObject("Alarm", "off")

        ## Checks upper limit and if statement is true turns on green LED and alarm
        if price > ULim and Alarm == "on":
            print "Alarm on for upper limit"
            #acomm.send_command("oga")
            setup.setObject("Alarm", "off")

        print " "
        time.sleep(3)
