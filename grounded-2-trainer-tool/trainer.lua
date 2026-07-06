local trainer = {}
local utils = require("utils")

function trainer:run(player, features)
    while true do
        io.write("> ")
        local cmd = io.read()
        if cmd == "god" then
            features.god_mode = not features.god_mode
            utils:notify("God Mode: " .. tostring(features.god_mode))
        elseif cmd == "stamina" then
            features.infinite_stamina = not features.infinite_stamina
            utils:notify("Infinite Stamina: " .. tostring(features.infinite_stamina))
        elseif cmd == "hunger" then
            features.no_hunger = not features.no_hunger
            utils:notify("No Hunger: " .. tostring(features.no_hunger))
        elseif cmd == "status" then
            print("Player HP: " .. player.health)
            print("Features:")
            for k, v in pairs(features) do
                print("  " .. k .. ": " .. tostring(v))
            end
        elseif cmd == "quit" then
            print("Exiting trainer.")
            break
        else
            print("Unknown command. Try: god, stamina, hunger, status, quit")
        end
    end
end

return trainer