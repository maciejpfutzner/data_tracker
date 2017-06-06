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
    with open('setupfile.txt', 'r') as json_file:
        setup = json.load(json_file)
        setup[Name] = Setting
    with open('setupfile.txt', 'w') as outfile:
        json.dump(setup, outfile)
    return

def main(argv=sys.argv):
    
    print argv
    
    usage = "usage: %prog [options]"
    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument("--Type", action='append')
    parser.add_argument("--Stock", action='append')
    parser.add_argument("--ULim", action='append')
    parser.add_argument("--LLim", action='append')
    parser.add_argument("--Alarm", action='append')
    parser.add_argument("--Reminder", action='append')
    options = parser.parse_args()
    
    with open('setupfile.txt') as json_file:
       setup = json.load(json_file)

    if(options.Type): Type = "".join(options.Type)
    else: Type = str(setup["Type"])
    if(options.Stock): StockName = "".join(options.Stock)
    else: StockName = str(setup["Stock"])
    if(options.ULim): ULim = "".join(options.ULim)
    else: ULim = float(setup["UpperLimit"])
    if(options.LLim): LLim = "".join(options.LLim)
    else: LLim = float(setup["LowerLimit"])
    if(options.Alarm): Alarm = "".join(options.Alarm)
    else: Alarm = str(setup["Alarm"])
    if(options.Reminder): Reminder = int("".join(options.Reminder))
    else: Reminder = -5
    
    setup = {'Type':Type, 'Stock':StockName, 'UpperLimit':ULim, 'LowerLimit':LLim, 'Alarm':Alarm, 'Reminder':setTimer(Reminder)}


    with open('setupfile.txt', 'w') as outfile:
        json.dump(setup, outfile)


if __name__ == "__main__":
    main()
