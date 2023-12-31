--Runs one job of parsing
local lfs = require("lfs")

local function runScript(folderName)
	local command = string.format("printf '#!/bin/bash\\n\\n"  ..
	"#SBATCH -p tiny\\n\\n" ..
	"apptainer exec --writable -f ../pythonContainer/ python3 /root/meleeCpus/parseFolder.py -i /root/meleeCpus/SlippiFiles/%s > ~/meleeCpus/parseOuts/%s.json'",
	folderName,folderName
)
	os.execute(command .. " | sbatch")

end

for file in lfs.dir("./SlippiFiles/") do
    runScript(file)
end


