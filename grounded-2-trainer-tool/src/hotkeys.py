import keyboard
from typing import Dict, Callable

class HotkeyManager:
    def __init__(self):
        self._hotkeys: Dict[str, Callable] = {}

    def register(self, key: str, callback: Callable) -> None:
        self._hotkeys[key] = callback
        keyboard.add_hotkey(key, callback)

    def unregister(self, key: str) -> None:
        if key in self._hotkeys:
            keyboard.remove_hotkey(key)
            del self._hotkeys[key]

    def clear_all(self) -> None:
        for key in list(self._hotkeys.keys()):
            self.unregister(key)

    def list_hotkeys(self) -> Dict[str, Callable]:
        return self._hotkeys.copy()