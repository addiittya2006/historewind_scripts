# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as Soup, Tag
import os
import requests

months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
days_month = [31,29,31,30,31,30,31,31,30,31,30,31]

for i in range(len(months)):
    for day in range(1, days_month[i]+1):
        today = months[i]+"_"+str(day)

        response = requests.get("http://en.wikipedia.org/wiki/"+str(today))
        soup = Soup(response.content, "html.parser")

        births_span = soup.find("span", {"id": "Deaths"})
        births_ul = births_span.parent.find_next_sibling()
        path = "out/"+str(today)
        if not os.path.exists(path):
            os.makedirs(path)
        target = open(os.path.join(path, "deaths.csv"), "w")

        for item in births_ul.find_all('li'):
            if isinstance(item, Tag):
                try:
                    target.write(unicode(item.text).encode('ascii', 'ignore').split()[0]+","+str(item).strip('<li>').strip('</li>').split("–")[1]+"\n")
                except:
                    try:
                        target.write(unicode(item.text).encode('ascii', 'ignore').split()[0]+","+str(item).strip('<li>').strip('</li>').split("--")[1]+"\n")
                    except:
                        try:
                            target.write(unicode(item.text).encode('ascii', 'ignore').split()[0]+","+str(item).strip('<li>').strip('</li>').split("-")[1]+"\n")
                        except:
                            try:
                                target.write(unicode(item.text).encode('ascii', 'ignore').split()[0]+","+str(item).strip('<li>').strip('</li>').split("－")[1]+"\n")
                            # print unicode(item.text).encode('ascii', 'ignore').split()[0]+","+str(item).strip('<li>').strip('</li>').split(" ")[1]
                            except:
                                print "***skipped "+unicode(item.text).encode('ascii', 'ignore').split()[0]
        print "written "+str(today)