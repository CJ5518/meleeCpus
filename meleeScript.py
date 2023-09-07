import melee, os,sys
import argparse


parser = argparse.ArgumentParser(description="Python utility to run arbitrary cpu battles in melee")
parser.add_argument("--test", help="Run the program in test mode, will print success or failure", action="store_true")
parser.add_argument("--player1", "-p1", help="ID of the character in port 1", type=int, default=None, required=True)
parser.add_argument("--player2", "-p2", help="ID of the character in port 2", type=int, default=None, required=True)
parser.add_argument("--stage", "-s", help="ID of the stage to play on", type=int, default=None, required=True)
parser.add_argument("--numGames", "-n", help="The number of games to play", type=int, default=None, required=True)
parser.add_argument("--outputdir", "-o", help="The output directory for our output data", type=str, default=None, required=True)

args = parser.parse_args()


charIDToEnum = []



console = melee.console.Console(fullscreen=False, path="/slippi-Ishiiruka/build/Binaries/")

console.run(exe_name="dolphin-emu", iso_path="/root/Documents/ProgrammingProjects/meleeCpus/melee.iso")

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

while True:
    gamestate = console.step()
    if gamestate is None:
        continue
    # Press buttons on your controller based on the GameState here!

    if gamestate.menu_state in [melee.Menu.IN_GAME, melee.Menu.SUDDEN_DEATH]:
        pass
    elif gamestate.menu_state in [melee.Menu.CHARACTER_SELECT]:
        melee.MenuHelper.choose_character(melee.enums.Character(args.player1), gamestate, controller)
        melee.MenuHelper.choose_character(melee.enums.Character(args.player2), gamestate, controller2, cpu_level=9, start=True)
    elif gamestate.menu_state in [melee.Menu.STAGE_SELECT]:
        pass
    else:
        melee.MenuHelper.choose_versus_mode(gamestate, controller)

