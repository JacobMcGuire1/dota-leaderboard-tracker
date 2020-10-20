
import json
import matplotlib.pyplot as plt
import os

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
        ranklists.append(ranklist)
    else:
        continue

linedict = dict()
for x in ranklists:
    for y in x[-15:]:
        print(y)
        point = y
        rank = point[0]
        team = point[1]
        name = point[2]
        key = team + name
        if (linedict.__contains__(team + name) and rank is not -1):
            linedict[team + name].append(rank)
        else:
            linedict[team + name] = [rank]


plt.ylabel('Rank')
plt.xlabel('Time')

c = 0
for x in list(linedict.keys()):
    plt.plot(linedict[x],  label=x)
    c += 1

plt.legend()
plt.show()


#plt.plot([10,9,8], [1, 2, 3])
#plt.ylabel('Rank')
#plt.xlabel('Time')
#plt.show()