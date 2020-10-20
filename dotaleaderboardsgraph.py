import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import json
import matplotlib.pyplot as plt
import time

def getPlayerList(region):
    session = HTMLSession()

    r = session.get('https://www.dota2.com/leaderboards#' + region)
    r.html.render(1,"",scrolldown=0, sleep=1)

    playerlistelement = r.html.find("#leaderboard_body", first=True)
    players = playerlistelement.find("tr", first=False)

    playerlist = []

    for x in reversed(players):
        team = x.find(".team_tag", first=True)
        name = x.find(".player_name", first=True)
        rank = x.find("td", first=True)

        nametext = ""
        teamtext = ""
        ranktext = ""
        ranknum = -1
        if (team is not None):
            teamtext = team.text
        if (name is not None):
            nametext = name.text
        if (rank is not None):
            ranktext = rank.text
            if (ranktext is not ""):
                ranknum = int(ranktext)

        #if (ranknum <= 50):
           # print(teamtext + nametext + ranktext)

        playerlist.append((ranknum, teamtext, nametext))

    return playerlist

playerlist = getPlayerList("europe")
json = json.dumps(playerlist)
f = open("./europe/" + str(time.time()) + ".json", "w")
f.write(json)
f.close()

#plt.plot(1, playerlist[0][0])#, label=(playerlist[0][1] + playerlist[0][2]))
#plt.plot(2, playerlist[1][0])#, label=(playerlist[1][1] + playerlist[1][2]))
#plt.plot(3, playerlist[2][0])#, label=(playerlist[2][1] + playerlist[2][2]))

""" plt.plot([10,9,8], [1, 2, 3])
plt.ylabel('Rank')
plt.xlabel('Time')
plt.show()
         """
