import getData as gd
import bitcoin_price as bp
import time

#-------------------------------------------------------#
if __name__ == '__main__':

    while True:
        
        with open('setupfile.txt') as json_file:
            setup = json.load(json_file)
    
        Type = setup["Type"]
        Stock = setup["Stock"]
        ULimit = setup["UpperLimit"]
        LLimit = setup["LowerLimit"]
        
        
        if( Type == "Stock"):
        
        
            gd.getPrice()
            gd.getTradeTime()
        print " "
            
        time.sleep(5)
