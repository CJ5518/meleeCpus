--Runs some numbers of replicates of cpu games on falcon


local function runBattles(p1, p2, stage, numGames, cpu1Lvl, cpu2Lvl)
	local command = string.format("printf '#!/bin/bash\\n\\n"  ..
	"#SBATCH --exclusive -p tiny\\n\\n" ..
	"mkdir ~/meleeCpus/SlippiFiles/Job_%%%%j/ \\n\\n" .. --The hilarious 4 percent signs to result in just one in the output
	"apptainer exec --fakeroot melee.sif python3 /meleeScript.py -p1 %d -p2 %d -s %d -n %d --p1cpu %d --p2cpu %d -o ~/SlippiFiles/Job_%%%%j/ --iso ~/meleeCpus/melee.iso\\n'",
	p1,p2,stage,numGames,cpu1Lvl,cpu2Lvl
)
	os.execute(command .. " | sbatch")
end


stages = {
	24,26,25,8,18,6
}

characters = {
	0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,20,21,22,23,24,25,26
}

local count = 0;

for _, id in pairs(characters) do
	for _, id2 in pairs(characters) do
		for _, stageId in pairs(stages) do
			runBattles(id, id2, stageId, 10, 9, 9);
			count = count + 1;
		end
	end
end

print("Running " .. tostring(count) .. " jobs");