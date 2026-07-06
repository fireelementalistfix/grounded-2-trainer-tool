local ui = {}

function ui:render_menu()
    print("=== Grounded 2 Trainer ===")
    print("Commands:")
    print("  god     - Toggle god mode")
    print("  stamina - Toggle infinite stamina")
    print("  hunger  - Toggle no hunger")
    print("  status  - Show player status")
    print("  quit    - Exit trainer")
    print("==========================")
end

return ui