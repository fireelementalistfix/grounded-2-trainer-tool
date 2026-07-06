import pytest
from unittest.mock import MagicMock, patch
from src.trainer import Grounded2Trainer

@pytest.fixture
def trainer():
    with patch('src.trainer.MemoryScanner') as mock_scanner:
        with patch('src.trainer.HotkeyManager') as mock_hotkeys:
            trainer = Grounded2Trainer()
            trainer.scanner = mock_scanner.return_value
            trainer.hotkeys = mock_hotkeys.return_value
            yield trainer

def test_toggle_infinite_health(trainer):
    assert trainer._features["infinite_health"] == False
    trainer.toggle_infinite_health()
    assert trainer._features["infinite_health"] == True
    trainer.scanner.write_int.assert_called_with(0x00A1B2C0, 9999)

def test_toggle_infinite_stamina(trainer):
    assert trainer._features["infinite_stamina"] == False
    trainer.toggle_infinite_stamina()
    assert trainer._features["infinite_stamina"] == True
    trainer.scanner.write_int.assert_called_with(0x00A1B2C4, 9999)

def test_toggle_no_hunger(trainer):
    assert trainer._features["no_hunger"] == False
    trainer.toggle_no_hunger()
    assert trainer._features["no_hunger"] == True
    trainer.scanner.write_int.assert_called_with(0x00A1B2C8, 9999)

def test_get_status(trainer):
    trainer.scanner.read_int.side_effect = [100, 200, 300]
    status = trainer.get_status()
    assert status["health"] == 100
    assert status["stamina"] == 200
    assert status["hunger"] == 300
    assert status["features"] == trainer._features

def test_setup_default_hotkeys(trainer):
    trainer.setup_default_hotkeys()
    assert trainer.hotkeys.register.call_count == 3
    trainer.hotkeys.register.assert_any_call("f1", trainer.toggle_infinite_health)
    trainer.hotkeys.register.assert_any_call("f2", trainer.toggle_infinite_stamina)
    trainer.hotkeys.register.assert_any_call("f3", trainer.toggle_no_hunger)

def test_cleanup(trainer):
    trainer.cleanup()
    trainer.hotkeys.clear_all.assert_called_once()
    trainer.scanner.close.assert_called_once()