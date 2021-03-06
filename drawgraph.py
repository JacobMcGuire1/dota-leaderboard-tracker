
import json
import matplotlib.pyplot as plt
import os
import datetime
from _datetime import date
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
import math

""" plt.plot([10,9,8], [1, 2, 3])
plt.ylabel('Rank')
plt.xlabel('Time')
plt.show()
         """


         
#need to egt timestamp




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
        if (end <= 1):
            end *= -1
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

def drawLines(linedict):
    plt.ylabel('Rank')
    plt.xlabel('Date/Time')
    for x in list(linedict.keys()):
        rankpairs = linedict[x]
        ranks = []
        times = []
        rankpairs.sort(key=lambda pair : pair[1])
        ranks = [pair[0] for pair in rankpairs]
        times = [datetime.datetime.fromtimestamp(float(pair[1])) for pair in rankpairs]
        if (len(rankpairs) > 0):
            plt.plot(times, ranks,  label=x)
            plt.annotate(str(ranks[0]) + ": " + x, xy = (times[0], ranks[0]),  xytext = (times[0], 0.15 + ranks[0]))
            if (len(rankpairs) > 1):
                plt.annotate(str(ranks[-1]), xy = (times[-1], ranks[-1]),  xytext = (times[-1], 0.15 + ranks[-1]))

def getRankListsFromFiles(pathtoranklists):
    ranklists = []
    for filename in os.listdir(pathtoranklists):
        if filename.endswith(".json"):
            f = open(pathtoranklists + filename, "r")
            ranklist = json.load(f)
            ranklists.append((ranklist, filename[:-5]))
        else:
            continue
    return ranklists

fig = plt.figure()
plot = fig.add_subplot(111)
currentplayerannotation = plt.annotate("tets", xy = (18555.678571548888, 20.800066229152872))
def on_plot_hover(event):
    global currentplayerannotation
    # Iterating over each data member plotted
    for curve in plot.get_lines():
        # Searching which data member corresponds to current mouse position
        if curve.contains(event)[0]:
            try:
                currentplayerannotation.remove()
            except:
                print("No annotation to remove")
            currentplayerannotation = plt.annotate(curve._label + ": " + str(math.floor(event.ydata)), xy = (event.xdata, event.ydata))
            #currentplayerannotation.set_position((event.xdata, event.ydata))

            #currentplayerannotation.set_position((event.xdata, event.ydata))
            #currentplayerannotation.text = curve._label
            #currentplayerannotation.xy = (event.xdata, event.ydata)
            #print ("over ", curve._label)
            fig.canvas.draw()

ranklists = getRankListsFromFiles("./europe/")

linedict = getLeaderboardPortion(0, 25)
#linedict = getPlayers(["dendi", "norv", "manolo", "hellshock", "5up"])

drawLines(linedict)


fig.canvas.mpl_connect('motion_notify_event', on_plot_hover)    



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