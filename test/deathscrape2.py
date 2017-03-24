# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as Soup, Tag
import os
import requests

months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
days_month = [31,29,31,30,31,30,31,31,30,31,30,31]

# for i in range(len(months)):
    # for day in range(1, days_month[i]+1):
        # today = months[i]+"_"+str(day)

response = requests.get("http://en.wikipedia.org/wiki/February_3")
        # response = requests.get("http://en.wikipedia.org/wiki/"+str(today))
        
# print "http://en.wikipedia.org/wiki/"+str(today)
soup = Soup(response.content, "html.parser")

births_span = soup.find("span", {"id": "Deaths"})
births_ul = births_span.parent.find_next_sibling()

today = "September_11"
path = "out/"+str(today)
if not os.path.exists(path):
    os.makedirs(path)
target = open(os.path.join(path, "deaths.csv"), "w")


for item in births_ul.find_all("li", recursive=False):
    # if isinstance(item, Tag):
        # for item in deaths_ul.find_all('li'):
    ul = item.find("ul")
    if ul:
        target.write(unicode(item.text).encode('ascii', 'ignore').split()[0] + ",")
        for ite in ul.find_all("li", recursive=False):
            target.write(str(ite).replace('<li>', '').replace('</li>', '') + '.')
        target.write("\n")
    else:
        target.write(unicode(item.text).encode('ascii', 'ignore').split()[0]+","+str(item).replace('<li>', '').replace('</li>', '').split("–")[1]+"\n")
        
        
        # ----*** Pass #1 ***----
        # ul = item.find("ul")
        # if ul:
            # print unicode(item.text).encode('ascii', 'ignore').split()[0] + ","
            # for ite in ul.find_all("li", recursive=False):
                # print str(ite).replace('<li>', '').replace('</li>', '') + '.'
                # print str(ite)
        # else:
            # print unicode(item.text).encode('ascii', 'ignore').split()[0]+","+str(item).replace('<li>', '').replace('</li>', '').split("–")[1]
        
        # ----** Failed Test #1 **----
        # try:
            # print unicode(item.text).encode('ascii', 'ignore').split()[0]+","+str(item).strip('<li>').strip('</li>').split("–")[1]+"\n"
        # except:
            # final = ''
            # for ite in item.find_all('li'):
                # final += str(ite).strip("<li>").strip("</li>")
            # print final
        
        # -----** Old Code Starts **------
        # print str(strip_tags(str(item)))
        # try:
            # print unicode(item.text).encode('ascii', 'ignore').split()[0]+","+str(item).strip('<li>').strip('</li>').split("–")[1]
        # except:
            # try:
                # print unicode(item.text).encode('ascii', 'ignore').split()[0]+","+str(item).strip('<li>').strip('</li>').split("--")[1]
            # except:
                # try:
                    # print unicode(item.text).encode('ascii', 'ignore').split()[0]+","+str(item).strip('<li>').strip('</li>').split("-")[1]
                # except:
                    # print unicode(item.text).encode('ascii', 'ignore').split()[0]+","+str(item).strip('<li>').strip('</li>').split(" ")[1]
                    # print "***skipped "+unicode(item.text).encode('ascii', 'ignore').split()[0]
        # print str(strip_tags(str(item))).strip('[').strip(']').split("–")
        # print str(item).strip('<li>').strip('</li>').split("–")[1]
        # print item.find_all('a')[0].text
        # print item
        # print unicode(item.text, 'utf-8')
        # .split("–")[0]
        # pos = str(item).find("–")
        # i = 0
        # while i < pos:
            # print str(item.text)[i],
            # i += 1
        # i = pos
        # leng = len(str(item))
        # while i != leng:
            # print str(item)[i],
            # i += 1