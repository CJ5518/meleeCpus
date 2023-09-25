local json = require("json")
local lfs = require("lfs")

local function decodeFile(path)
    local file = io.open("./parseOuts/" .. path,"r")
    return json.decode(file:read("a"))
end

local master = {};

local function consolidate(obj)
    for i,v in pairs(obj) do
        if master[i] then
            for i2,v2 in pairs(v) do
                if master[i][i2] then
                    master[i][i2] = master[i][i2] + v2
                else
                    master[i][i2] = v2
                end
            end
        else
            master[i] = {}
            for i2, v2 in pairs(v) do
                master[i][i2] = v2
            end
        end
    end
end

local function forAllFiles(root)
    for file in lfs.dir(root) do
        if file ~= "." and file ~= ".." then
            local obj = decodeFile(file)
            consolidate(obj)
        end
    end
    print(json.encode(master))
end

forAllFiles("./parseOuts/")
