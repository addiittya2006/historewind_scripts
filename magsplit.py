import os
import json


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
days_month = [31,29,31,30,31,30,31,31,30,31,30,31]

for i in range(len(months)):
    for day in range(1, days_month[i]+1):
        date = months[i]+"_"+str(day)


        mornmagdict = {}
        evemagdict = {}
        with open(os.path.join(__location__, "out/"+str(date)+"/mag.json"), "r") as filev:
            json_data = json.load(filev)
            try:
                lst = []
                for item in range(0, 4):
                    # morning
                    lst.append(json_data["births"][item])
                mornmagdict["births"] = lst
                # evening
                lst = []
                lst.append(json_data["births"][4])
                evemagdict["births"] = lst
            except:
                print "bb"+date

            # morning
            try:
                lst = []
                lst.append(json_data["deaths"][0])
                mornmagdict["deaths"] = lst
                lst = []
                for item in range(1, 5):
                # evening
                    lst.append(json_data["deaths"][item])
                evemagdict["deaths"] = lst
            except:
                print "dd"+date

            # morning
            try:
                lst = []
                for item in range(0, 5):
                    lst.append(json_data["events"][((item*2)+1)])
                evemagdict["events"] = lst
                # eve
                lst = []
                for item in range(0, 5):
                    lst.append(json_data["events"][(item*2)])
                mornmagdict["events"] = lst
            except:
                print "ee"+date
            
        targetm = open(os.path.join(__location__, "out/"+str(date)+"/morn_digest.json"), "w")
        targetm.write(json.dumps(mornmagdict))
        targete = open(os.path.join(__location__, "out/"+str(date)+"/eve_digest.json"), "w")
        targete.write(json.dumps(evemagdict))
        