import json
import sys
import argparse
import datetime
from datetime import timedelta

#-------------------------------------------------------#

def setTimer(Mins):
    now = datetime.datetime.now()
    Timer = now + datetime.timedelta(minutes = Mins)
    return Timer.isoformat()

def setObject(Name, Setting):
    with open('setupfile.json', 'r') as json_file:
        setup = json.load(json_file)
        setup[Name] = Setting
    with open('setupfile.json', 'w') as outfile:
        json.dump(setup, outfile)
    return

def main(argv=sys.argv):
    
    print argv
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--Type", action='append')
    parser.add_argument("--Stock", action='append')
    parser.add_argument("--ULim", action='append')
    parser.add_argument("--LLim", action='append')
    parser.add_argument("--Alarm", action='append')
    parser.add_argument("--Reminder", action='append')
    options = parser.parse_args()
    
    try:
        with open('setupfile.json') as json_file:
            setup = json.load(json_file)

        if(options.Type): Type = "".join(options.Type)
        else: Type = str(setup["Type"])
        if(options.Stock): StockName = "".join(options.Stock)
        else: StockName = str(setup["Stock"])
        if(options.ULim): ULim = "".join(options.ULim)
        else: ULim = str(setup["UpperLimit"])
        if(options.LLim): LLim = "".join(options.LLim)
        else: LLim = str(setup["LowerLimit"])
        if(options.Alarm): Alarm = "".join(options.Alarm)
        else: Alarm = str(setup["Alarm"])
        if(options.Reminder): Reminder = int("".join(options.Reminder))
        else: Reminder = -5
        
        setup = {'Type':Type, 'Stock':StockName, 'UpperLimit':ULim, 'LowerLimit':LLim, 'Alarm':Alarm, 'Reminder':setTimer(Reminder)}

    except IOError:
        # If no file exists, start from zero
        setup = {'Type':'Stock', 'Stock':'AAPL', 'UpperLimit':'160', 'LowerLimit':'140', 'Alarm':'off'}


    with open('setupfile.json', 'w') as outfile:
        json.dump(setup, outfile)


if __name__ == "__main__":
    main()
