import os
import re
import json
import operator
from bs4 import BeautifulSoup as Soup, Tag

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

bdict = {}
edict = {}
ddict = {}
magdict = {}

def prepare_index(date):
    with open(os.path.join(__location__, "out/"+str(date)+"/births.csv"), "r") as filev:
        for line in filev:
            m = str(line).split("**")
            bdict[m[0]] = m[1]
    
    with open(os.path.join(__location__, "out/"+str(date)+"/events.csv"), "r") as filev:
        for line in filev:
            m = str(line).split("**")
            edict[m[0]] = m[1]
    
    with open(os.path.join(__location__, "out/"+str(date)+"/deaths.csv"), "r") as filev:
        for line in filev:
            m = str(line).split("**")
            ddict[m[0]] = m[1]


def get_news(event, date, year):
    prepare_index(date)
    if event == 1:
        return bdict.get(year)
    elif event == 2:
        return edict.get(year)
    elif event == 3:
        return ddict.get(year)
    else:
        print "error"
        

months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
days_month = [31,29,31,30,31,30,31,31,30,31,30,31]

for i in range(len(months)):
    for day in range(1, days_month[i]+1):
        date = months[i]+"_"+str(day)
        magdict["date"] = date

        with open(os.path.join(__location__, "out/"+str(date)+"/scored.txt"), "r") as scorefile:
            string = scorefile.read()
            scores = eval(string)
            birthscores = scores.get("births")
            eventscores = scores.get("events")
            deathscores = scores.get("deaths")
            
            # print birthscores
            # sortedb = reversed(sorted(birthscores.items(), key=lambda x:x[1]))
            sortedb = sorted(birthscores, key=birthscores.get, reverse=True)[:5]
            sortede = sorted(eventscores, key=eventscores.get, reverse=True)[:10]
            sortedd = sorted(deathscores, key=deathscores.get, reverse=True)[:5]
            # print sortedb
            # print sortedd
            # print sortede
            lst = []
            for item in sortedb:
                tempdict = {}
                tempdict[item] = get_news(1, date, item)
                lst.append(tempdict)
            magdict["births"] = lst
            lst = []
            for item in sortedd:
                tempdict = {}
                tempdict[item] = get_news(3, date, item)
                lst.append(tempdict)
            magdict["deaths"] = lst
            lst = []
            for item in sortede:
                tempdict = {}
                tempdict[item] = get_news(2, date, item)
                lst.append(tempdict)
            magdict["events"] = lst
        
        target = open(os.path.join(__location__, "out/"+str(date)+"/mag.json"), "w")
        target.write(json.dumps(magdict))
        # print date
