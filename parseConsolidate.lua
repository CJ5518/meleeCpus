local json = require("json")
local lfs = require("lfs")


local function decodeGenericFile(path)
    local file = io.open(path,"r")
    return json.decode(file:read("a"))
end

local function decodeFile(path)
    return decodeGenericFile("./parseOuts/" .. path)
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
    local count = 0;
    for i, v in pairs(master) do
        for i2, v2 in pairs(v) do
            count = count + v2;
        end
    end
    print("Number of games: " .. tostring(count))

    local file = io.open("out.csv", "w")
    local charNameArray = decodeGenericFile("characterIds.json")

    file:write("Winrate,")
    for q = 0,25 do
        if master[tostring(q)] then
            file:write("=IMAGE(\"" .. charNameArray[tostring(q)][2] .. "\")")
            file:write(",")
        end
    end
    file:write("\n")
    for q = 0,25 do
        local matchups = master[tostring(q)]
        if matchups then
            file:write("=IMAGE(\"" .. charNameArray[tostring(q)][2] .. "\")")
            file:write(",")
            for i = 0,25 do
                if matchups[tostring(i)] then
                    local wins = matchups[tostring(i)]
                    local losses = master[tostring(i)][tostring(q)]
                    local games = wins + losses;
                    local winrate = wins / games;
                    if q == i then
                        winrate = .5
                    end
                    file:write(winrate)
                    file:write(",");
                end
            end
            file:write("\n");
        end
    end
end

forAllFiles("./parseOuts/")
