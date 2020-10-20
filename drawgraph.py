
import json
import matplotlib.pyplot as plt
import os
import datetime
from _datetime import date
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter

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


def getPlayers(players):
    linedict = dict()
    lowerplayers = []
    for x in players:
        lowerplayers.append(x.lower())
    players = lowerplayers
    for ranklist, time in ranklists:
        matches = [x for x in ranklist if (x[2].lower() in players)]
        addPointsToDict(matches, time, linedict)
    return linedict

def getLeaderboardPortion(start, end):
    linedict = dict()
    for ranklist, time in ranklists: 
        if (start <= 1):
            ranklist = ranklist[-end:]
        else:
            ranklist = ranklist[-end:-start]
        addPointsToDict(ranklist, time, linedict)
    return linedict

def addPointsToDict(ranklist, time, linedict):
    for point in ranklist:
        rank = point[0]
        team = point[1].replace("$$", "")
        name = point[2].replace("$$", "")
        key = (team + name)
        if (key in linedict and rank is not -1):
            linedict[key].append((rank, time))
        else:
            linedict[key] = [(rank, time)]


linedict = getLeaderboardPortion(0, 25)
#linedict = getPlayers(["dendi", "norv", "manolo", "hellshock"])


plt.ylabel('Rank')
plt.xlabel('Date/Time')

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
    if (latestrank != -1):
        plt.plot(times, ranks,  label=x)
        plt.annotate(str(latestrank) + ": " + x, xy = (times[-1], ranks[-1]),  xytext = (times[-1], 0.15 + ranks[-1]))

#date_form = DateFormatter("%m-%d")
#\fig, ax = plt.subplots()

#ax.xaxis.set_major_formatter(date_form)

plt.gcf().autofmt_xdate()

#f, ax = plt.subplots(1)
#ax.set_ylim(bottom=100)
#plt.legend(loc='upper left')
plt.show()


#plt.plot([10,9,8], [1, 2, 3])
#plt.ylabel('Rank')
#plt.xlabel('Time')
#plt.show()