import os
import re
from bs4 import BeautifulSoup as Soup, Tag
from pymongo import MongoClient

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
days_month = [31,29,31,30,31,30,31,31,30,31,30,31]

ranks = {}

scores = open(os.path.join(__location__, "pagetitlerank.txt"), "r")

client = MongoClient('localhost', 27017)
# client = MongoClient('mongodb://root:adi21@127.0.0.1')

while True:
    name = scores.readline().strip("\n")
    score = scores.readline().strip("\n")
    # name.strip("\\n")
    # score.strip("\\n")
    ranks[name] = score
    if not name:
        break

def imagequery(title):
    strip = title.replace("_", " ")
    imageq = client.wiki.pageimageshigh.find_one({"_id": strip})
    if imageq != None:
        return str(imageq.get('thumburl'))
    else:
        return strip
    

def rankquery(title):
    # print "querying.."
    strip = title.replace("_", " ")
    return ranks.get(strip)
    # for line in scores:
    # ranks = {}

for i in range(len(months)):
    for day in range(1, days_month[i]+1):
        # date = months[i]+"_"+str(day)
# for i in range(0, 0):
    # for day in range(1, 32):
        date = months[i]+"_"+str(day)
        elinescore = {}
        dlinescore = {}
        blinescore = {}
        eimg = {}
        dimg = {}
        bimg = {}

        cluster = {}
        imagecluster = {}

        with open(os.path.join(__location__, "out/"+str(date)+"/events.csv"), "r") as eventsfile:
            for line in eventsfile:
                m = str(line).split("**")
                year = m[0]
                soup = Soup(m[1], 'html.parser')
                k = 0
                total = 0
                num1 = 0
                for link in soup.findAll('a'):
                    # print link.get('href')
                    if re.compile("/wiki/(.*)").match(link.get('href')) != None:
                        query = re.compile("/wiki/(.*)").match(link.get('href')).groups(0)[0]
                        # print query
                    if rankquery(query) != None:
                        num = int(rankquery(query))
                    else:
                        num = 0
                    
                    if num > num1:
                        maxelem = query
                    maxelem = imagequery(maxelem)
                    
                        # print num
                    total += int(num)
                    k += 1
                    # for()
                    # Calculate Weighted Average for the line
                if k > 0:
                    # print total, k
                    avg = total/k
                    elinescore[year] = avg
                    eimg[year] = maxelem
                else:
                    print total
            cluster["events"] = elinescore
            imagecluster["events"] = eimg
        # print date


        with open(os.path.join(__location__, "out/"+str(date)+"/deaths.csv"), "r") as deathsfile:
            for line in deathsfile:
                m = str(line).split("**")
                year = m[0]
                soup = Soup(m[1], "html.parser")
                k = 0
                total = 0
                num1 = 0
                for link in soup.findAll('a'):
                    # print link.get('href')
                    if re.compile("/wiki/(.*)").match(link.get('href')) != None:
                        query = re.compile("/wiki/(.*)").match(link.get('href')).groups(0)[0]
                    # Query Here
                    # print query
                    if rankquery(query) != None:
                        num = int(rankquery(query))
                    else:
                        num = 0
                    if num > num1:
                        maxelem = query
                    maxelem = imagequery(maxelem)
                    # Calculate Weighted Average for the line
                    total += int(num)
                    k += 1
                if k > 0:
                    avg = total/k
                    dlinescore[year] = avg
                    dimg[year] = maxelem
                else:
                    print total
            cluster["deaths"] = dlinescore
            imagecluster["deaths"] = dimg
       

        with open(os.path.join(__location__, "out/"+str(date)+"/births.csv"), "r") as birthsfile:
            for line in birthsfile:
                m = str(line).split("**")
                soup = Soup(m[1], "html.parser")
                k = 0
                total = 0
                num1 = 0
                year = m[0]
                for link in soup.findAll('a'):
                    # print link.get('href')
                    if re.compile("/wiki/(.*)").match(link.get('href')) != None:
                        query = re.compile("/wiki/(.*)").match(link.get('href')).groups(0)[0]
                    # Query Here
                    # print query
                    if rankquery(query) != None:
                        num = int(rankquery(query))
                    else:
                        num = 0
                    if num > num1:
                        maxelem = query
                    maxelem = imagequery(maxelem)

                    total += int(num)
                    k += 1
                    # Calculate Weighted Average for the line
                if k > 0:
                    avg = total/k
                    blinescore[year] = avg
                    bimg[year] = maxelem
                else:
                    print total
            # print linescore
            cluster["births"] = blinescore
            imagecluster["births"] = bimg

        # Write Cluster to file
        # print "Writing..."
        savepath = os.path.join(__location__, "out/"+str(date))
        target = open(os.path.join(savepath, "scored.txt"), "w")
        imgtarget = open(os.path.join(savepath, "imager.txt"), "w")
        target.write(str(cluster))
        imgtarget.write(str(imagecluster))
        
                # print "**"
            # print "++"
        # print date
    # print "_____"