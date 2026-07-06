local trainer = require("trainer")
local ui = require("ui")
local utils = require("utils")

function Main()
    print("Grounded 2 Trainer Tool v1.0")
    print("Initializing...")
    local player = { health = 100, stamina = 100, hunger = 50 }
    local features = {
        god_mode = false,
        infinite_stamina = false,
        no_hunger = false
    }
    ui:render_menu()
    trainer:run(player, features)
end

Main()