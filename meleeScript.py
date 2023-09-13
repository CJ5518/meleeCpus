import melee, os,sys
import argparse


#Definitely a better way to do this, but this was easiest

parser = argparse.ArgumentParser(description="Python utility to run arbitrary cpu battles in melee")
parser.add_argument("--test", help="Run the program in test mode, will print success or failure", action="store_true")
parser.add_argument("--player1", "-p1", help="ID of the character in port 1", type=int, default=None, required=True)
parser.add_argument("--player2", "-p2", help="ID of the character in port 2", type=int, default=None, required=True)
parser.add_argument("--stage", "-s", help="ID of the stage to play on", type=int, default=None, required=True)
parser.add_argument("--numGames", "-n", help="The number of games to play", type=int, default=None, required=True)
parser.add_argument("--p1cpu", help="CPU level of player 1", type=int, default=9)
parser.add_argument("--p2cpu", help="CPU level of player 2", type=int, default=9)
parser.add_argument("--iso", "-i", help="Path to the melee ISO", type=str, default="/melee.iso")
parser.add_argument("--outputDir", "-o", help="Path to the slippi file output dir", type=str, default=None, required=True)

args = parser.parse_args()



console = melee.console.Console(fullscreen=False, path="/slippi-Ishiiruka/build/Binaries/", gfx_backend="Null", replay_directory=args.outputDir)

console.run(exe_name="dolphin-emu-nogui", iso_path=args.iso, command=["xvfb-run","-a"])

controller = melee.Controller(console=console, port=1)
controller2 = melee.Controller(console=console,port=2)

# Connect to the console
print("Connecting to console...")
if not console.connect():
	print("ERROR: Failed to connect to the console.")
	sys.exit(-1)
print("Console connected")


print("Connecting controller to console...")
if not controller.connect():
	print("ERROR: Failed to connect the controller.")
	sys.exit(-1)
print("Controller connected")

controller2.connect()

charSelectCount = 0
inStageFlag = False
runCount = 0
print("About to start stepping console")
while True:
	gamestate = console.step()
	if gamestate is None:
		continue
	# Press buttons on your controller based on the GameState here!

	if gamestate.menu_state in [melee.Menu.IN_GAME, melee.Menu.SUDDEN_DEATH]:
		if inStageFlag:
			print("Made it into a match")
			runCount += 1
			inStageFlag = False
	elif gamestate.menu_state in [melee.Menu.CHARACTER_SELECT]:

		#check if we've ran the requisite number of games
		if runCount >= args.numGames:
			break
		#Using start is weird when multiple cpus are involved
		doStart = False
		charSelectCount += 1
		if charSelectCount >= 60 * 5:
			doStart = True
		melee.MenuHelper.choose_character(melee.enums.Character(args.player1), gamestate, controller, cpu_level=9, start=doStart)
		melee.MenuHelper.choose_character(melee.enums.Character(args.player2), gamestate, controller2, cpu_level=9, start=doStart)
	elif gamestate.menu_state in [melee.Menu.STAGE_SELECT]:
		charSelectCount = 0
		inStageFlag = True
		melee.MenuHelper.choose_stage(melee.enums.Stage(args.stage), gamestate, controller)
	else:
		melee.MenuHelper.choose_versus_mode(gamestate, controller)


try:
	#This seems to error and not kill the dolphin process
	console.stop()
except:
	os.system("pkill dolphin")
	os.system("pkill dolphin")
	os.system("pkill Xvfb")
	os.system("pkill Xvfb")


