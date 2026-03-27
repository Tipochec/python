# controllers/game_controller.py
from models.game_state import GameState
from utils.file_manager import save_game, load_game
from config import DATA_FILE


class GameController:
    def __init__(self):
        self.state = GameState()
        self.load()
    
    def load(self) -> None:
        """Загружает сохранение"""
        data = load_game(DATA_FILE)
        self.state.set_coins(data.get("coins", 0))
        self.state.set_click_power(data.get("click_power", 1))
    
    def save(self) -> None:
        """Сохраняет игру"""
        data = {
            "coins": self.state.get_coins(),
            "click_power": self.state.get_click_power()
        }
        save_game(data, DATA_FILE)
    
    def add_coins(self, amount: int) -> None:
        """Добавляет монеты"""
        self.state.add_coins(amount)
        self.save()
    
    def get_coins(self) -> int:
        return self.state.get_coins()
    
    def get_click_power(self) -> int:
        return self.state.get_click_power()
    
    def set_click_power(self, value: int) -> None:
        self.state.set_click_power(value)
        self.save()
    
    def reset(self) -> None:
        """Сброс игры"""
        self.state.set_coins(0)
        self.state.set_click_power(1)
        self.save()