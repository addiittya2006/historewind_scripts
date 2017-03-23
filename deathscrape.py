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

        deaths_span = soup.find("span", {"id": "Deaths"})
        deaths_ul = deaths_span.parent.find_next_sibling()
        path = "out/"+str(today)
        if not os.path.exists(path):
            os.makedirs(path)
        target = open(os.path.join(path, "deaths.csv"), "w")

        for item in deaths_ul.find_all('li', recursive=False):
            ul = item.find("ul")
            if ul:
                target.write(unicode(item.text).encode('ascii', 'ignore').split()[0] + "**")
                for ite in ul.find_all("li", recursive=False):
                    target.write(str(ite).replace('<li>', '').replace('</li>', '') + '.')
                target.write("\n")
            else:
                try:
                    target.write(unicode(item.text).encode('ascii', 'ignore').split()[0]+"**"+str(item).replace('<li>', '').replace('</li>', '').split("–", 1)[1]+"\n")
                except:
                    try:
                        target.write(unicode(item.text).encode('ascii', 'ignore').split()[0]+"**"+str(item).replace('<li>', '').replace('</li>', '').split("-", 1)[1]+"\n")
                    except:
                        print "***skipped "+unicode(item.text).encode('ascii', 'ignore').split()[0]
        print "written "+str(today)