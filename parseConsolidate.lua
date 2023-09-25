local json = require("json")
local lfs = require("lfs")

local function decodeFile(path)
    local file = io.open("./parseOuts/" .. path,"r")
    return json.decode(file:read("a"))
end


local function forAllFiles(root)
    for file in lfs.dir(root) do
        if file ~= "." and file ~= ".." then
            local obj = decodeFile(file)
            print(obj)
        end
    end
end

forAllFiles("./parseOuts/")
