local utils = {}

function utils:notify(msg)
    print("[TRAINER] " .. msg)
end

function utils:clamp(val, min, max)
    if val < min then return min end
    if val > max then return max end
    return val
end

return utils