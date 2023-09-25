local json = require("json")
local lfs = require("lfs")

local function decodeFile(path)
    local file = io.open(path,"r")
    return json.decode(file:read("a"))
end


local function forAllFiles(root)
    for file in lfs.dir(root) do
        local obj = decodeFile(file)
        print(obj)
    end
end

forAllFiles("./parseOuts/")
