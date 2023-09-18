import os
from slippi import Game

#Script assumes the following file structure:
#./
#./SlippiFiles/
#./SlippiFiles/Job_1111/Game_##.slp
#./SlippiFiles/Job_2222/Game_##.slp
#./SlippiFiles/Job_3333/Game_##.slp

#Do something with a .slp file
def parseGame(path):
    try:
        game = Game(path, skip_frames=True)
        print("Parsed game " + path)
    except:
        print("Couldn't parse replay " + path)



def handleDir(path):
    for root,dirs,files in os.walk():
        for file in files:
            print(root + file)

for root, dirs, files in os.walk():
    for dire in dirs:
        handleDir(root + dire)
    break