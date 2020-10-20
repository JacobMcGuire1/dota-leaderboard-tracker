
import json
import matplotlib.pyplot as plt
import os
import datetime
from _datetime import date

""" plt.plot([10,9,8], [1, 2, 3])
plt.ylabel('Rank')
plt.xlabel('Time')
plt.show()
         """


         
#need to egt timestamp

directory = "./europe/"
ranklists = []
for filename in os.listdir(directory):
    if filename.endswith(".json"):
        f = open(directory + filename, "r")
        ranklist = json.load(f)
        ranklists.append((ranklist, filename[:-5]))
    else:
        continue

linedict = dict()
for ranklist, time in ranklists:
    for y in ranklist[-15:]:
        print(y)
        point = y
        rank = point[0]
        team = point[1]
        name = point[2]
        key = team + name
        if (linedict.__contains__(team + name) and rank is not -1):
            linedict[team + name].append((rank, time))
        else:
            linedict[team + name] = [(rank, time)]
        


plt.ylabel('Rank')
plt.xlabel('Time')

for x in list(linedict.keys()):
    
    rankpairs = linedict[x]
    ranks = []
    times = []
    latest = 0.0
    latestrank = 0
    for rank, time in rankpairs:
        timestamp = float(time)
        
        if (timestamp > latest):
            latest = timestamp
            latestrank = rank

        ranks.append(rank)
        times.append(datetime.datetime.fromtimestamp(timestamp))
    print(x)
    print(times)
    print(ranks)
    plt.plot(times, ranks,  label=x)
    plt.annotate(x + "daowindion", xy = (latest, latestrank), )
    plt.annotate(x, xy = (times[0], ranks[0]),  xytext = (times[0], 1.01*ranks[0]))
    #print(rankpair)
    
plt.gcf().autofmt_xdate()
#plt.legend(loc='upper left')
plt.show()


#plt.plot([10,9,8], [1, 2, 3])
#plt.ylabel('Rank')
#plt.xlabel('Time')
#plt.show()