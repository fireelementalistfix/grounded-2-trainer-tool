from .memory_scanner import MemoryScanner
from .hotkeys import HotkeyManager
from typing import Dict, Any

class Grounded2Trainer:
    def __init__(self):
        self.scanner = MemoryScanner()
        self.hotkeys = HotkeyManager()
        self._features: Dict[str, bool] = {
            "infinite_health": False,
            "infinite_stamina": False,
            "no_hunger": False,
        }
        self._addresses = {
            "health": 0x00A1B2C0,
            "stamina": 0x00A1B2C4,
            "hunger": 0x00A1B2C8,
        }

    def toggle_infinite_health(self) -> None:
        self._features["infinite_health"] = not self._features["infinite_health"]
        if self._features["infinite_health"]:
            self.scanner.write_int(self._addresses["health"], 9999)

    def toggle_infinite_stamina(self) -> None:
        self._features["infinite_stamina"] = not self._features["infinite_stamina"]
        if self._features["infinite_stamina"]:
            self.scanner.write_int(self._addresses["stamina"], 9999)

    def toggle_no_hunger(self) -> None:
        self._features["no_hunger"] = not self._features["no_hunger"]
        if self._features["no_hunger"]:
            self.scanner.write_int(self._addresses["hunger"], 9999)

    def get_status(self) -> Dict[str, Any]:
        return {
            "features": self._features.copy(),
            "health": self.scanner.read_int(self._addresses["health"]),
            "stamina": self.scanner.read_int(self._addresses["stamina"]),
            "hunger": self.scanner.read_int(self._addresses["hunger"]),
        }

    def setup_default_hotkeys(self) -> None:
        self.hotkeys.register("f1", self.toggle_infinite_health)
        self.hotkeys.register("f2", self.toggle_infinite_stamina)
        self.hotkeys.register("f3", self.toggle_no_hunger)

    def cleanup(self) -> None:
        self.hotkeys.clear_all()
        self.scanner.close()