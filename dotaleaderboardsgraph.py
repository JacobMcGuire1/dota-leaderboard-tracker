import requests
from requests_html import HTMLSession
import json
import time
import sqlite3


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
            if (ranktext != ""):
                ranknum = int(ranktext)
        playerlist.append((ranknum, teamtext, nametext))
    return playerlist

playerlist = getPlayerList("europe")
json = json.dumps(playerlist)
f = open("./europe/" + str(time.time()) + ".json", "w")
f.write(json)
f.close()
