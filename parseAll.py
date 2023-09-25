import os



for root, dirs, files in os.walk("./SlippiFiles/"):
    for dire in dirs:
        os.system("lua parseRunner.lua " + dire)
    break

