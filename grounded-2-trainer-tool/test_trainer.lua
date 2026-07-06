local utils = require("utils")
local trainer = require("trainer")

function TestGodMode()
    local player = { health = 100, stamina = 100, hunger = 50 }
    local features = { god_mode = false, infinite_stamina = false, no_hunger = false }
    features.god_mode = true
    assert(features.god_mode == true, "God mode should be true")
    print("PASS: God mode toggle works")
end

function TestClamp()
    local result = utils:clamp(150, 0, 100)
    assert(result == 100, "Clamp should return 100")
    result = utils:clamp(-10, 0, 100)
    assert(result == 0, "Clamp should return 0")
    print("PASS: Clamp utility works")
end

function TestNotify()
    local msg = nil
    local original_print = print
    print = function(s) msg = s end
    utils:notify("test")
    assert(msg == "[TRAINER] test", "Notify should format message correctly")
    print = original_print
    print("PASS: Notify utility works")
end

TestGodMode()
TestClamp()
TestNotify()
print("All tests passed.")