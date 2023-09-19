import os
import signal
from slippi import Game
from slippi.event import StateFlags

#Script assumes the following file structure:
#./
#./SlippiFiles/
#./SlippiFiles/Job_1111/Game_##.slp
#./SlippiFiles/Job_2222/Game_##.slp
#./SlippiFiles/Job_3333/Game_##.slp


#matchups[p0][p1] = Number of times char0 (p0) beat char1 (p1)
#This also means matchups[p1][p0] is number of times char0 lost to char1
#Number of games played between the two chars is the two above added.
matchups = {}

#Returns 0 if the player in port 0 won, and 1 otherwise
def getWinner(game):
    port0 = game.frames[-1].ports[0].leader.post.flags & StateFlags.DEAD
    if port0 == StateFlags.DEAD:
        return 0
    else:
        return 1

#Do something with a .slp file
def parseGame(path):
    try:
        game = Game(path)
        p0 = int(game.start.players[0].character)
        p1 = int(game.start.players[1].character)
        winnerPort = getWinner(game)

        #Make sure the structure of the dict is ready
        if p0 not in matchups:
            matchups[p0] = {}
        if p1 not in matchups[p0]:
            matchups[p0][p1] = 0
        if p1 not in matchups:
            matchups[p1] = {}
        if p0 not in matchups[p1]:
            matchups[p1][p0] = 0

        if getWinner(game) == 0:
            matchups[p0][p1] += 1
        else:
            matchups[p1][p0] += 1
    except Exception as e:
        print("Couldn't parse replay " + path)
        print(e)


def signal_handler(sig, frame):
    print("Exiting")
    os.exit(0)

signal.signal(signal.SIGINT, signal_handler)


def handleDir(path):
    for root,dirs,files in os.walk(path):
        for file in files:
            parseGame(root + "/" + file)

for root, dirs, files in os.walk("./SlippiFiles/"):
    for dire in dirs:
        handleDir(root + dire)
    break

print(matchups)
