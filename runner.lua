--Runs some numbers of replicates of cpu games on falcon


local function runBattles(p1, p2, stage, numGames, cpu1Lvl, cpu2Lvl)
	local command = string.format("printf '#!/bin/bash\\n\\n"  ..
	"#SBATCH --exclusive -p tiny\\n\\n" ..
	"apptainer exec --fakeroot melee.sif python3 /meleeScript.py -p1 %d -p2 %d -s %d -n %d --p1cpu %d --p2cpu %d\\n'",
	p1,p2,stage,numGames,cpu1Lvl,cpu2Lvl
)
	print(command .. " | sbatch")
end


stages = {
	24,26,25,8,18,6
}

characters = {
	0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,20,21,22,23,24,25,26
}

runBattles(1,2,24,2,9,9)
runBattles(1,2,24,2,9,9)
runBattles(1,2,24,2,9,9)
runBattles(1,2,24,2,9,9)
runBattles(1,2,24,2,9,9)
runBattles(1,2,24,2,9,9)
runBattles(1,2,24,2,9,9)
runBattles(1,2,24,2,9,9)
