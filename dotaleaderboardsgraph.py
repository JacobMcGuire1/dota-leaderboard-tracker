from datetime import datetime
import requests
from requests_html import HTMLSession
import json
import time
import sqlite3

con = sqlite3.connect('/home/jacob/scripts/dota-leaderboard-tracker/ranks.db')
cur = con.cursor()

def updateRanks(region):
    session = HTMLSession()

    r = session.get('https://www.dota2.com/leaderboards#' + region + "-0")
    r.html.render(1,"",scrolldown=0, sleep=1)

    timestamp = str(int(round(time.time())))
    cur.execute("INSERT INTO timestamps VALUES (?)", (timestamp,))

    cur.execute("INSERT OR IGNORE INTO regions VALUES (?)", (region.lower(),))

    playerlistelement = r.html.find("#leaderboard_body", first=True)
    players = playerlistelement.find("tr", first=False)

    #playerlist = []

    for x in reversed(players):
        foundarank = False
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
        if ((not nametext == "") and (not ranktext == "")):
            foundarank = True
            cur.execute("INSERT INTO ranks (timestamp, region, rank, team, name) VALUES (?, ? ,?, ?, ?)", (timestamp, region, ranktext, teamtext, nametext))
    
    con.commit()
    if (foundarank):
        print("Successfully collected at least one rank from region: "  + region + ".")
    time.sleep(1)

print()
print(datetime.now().strftime('%a %b %d %H:%M:%S %Z %Y'))
updateRanks("europe")
updateRanks("americas")
updateRanks("se_asia")
updateRanks("china")

con.close()