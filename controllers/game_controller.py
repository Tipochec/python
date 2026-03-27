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
        self.state.set_upgrades_bought(data.get("upgrades_bought", 0))
        self.state.set_auto_clickers(data.get('auto_clickers', 0))
    
    def save(self) -> None:
        """Сохраняет игру"""
        data = {
            "coins": self.state.get_coins(),
            "click_power": self.state.get_click_power(),
            "upgrades_bought": self.state.get_upgrades_bought(),
            "auto_clickers": self.state.get_auto_clickers()
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
        
    def buy_click_upgrade(self, cost_upgrate: int) -> bool:
        cost_upgrate = self.get_upgrade_cost()
        if self.state.get_coins() >= cost_upgrate:
            self.add_coins(-cost_upgrate)
            self.state.set_click_power(self.state.get_click_power() + 1)
            self.state.add_upgrade()
            self.save()
            return True
        return False
    
    def get_upgrade_cost(self):
        return 50 + self.state.get_upgrades_bought() * 10
    
    def get_auto_clicker_cost(self):
        """Стоимость следующего автокликера"""
        count = self.state.get_auto_clickers()
        return 100 + count * 50
    
    def buy_auto_clicker(self):
        cost = self.get_auto_clicker_cost()
        if self.state.get_coins() >= cost:
            self.state.add_coins(-cost)
            self.state.add_auto_clicker()
            self.save()
            return True
        return False
    
    def get_passive_income_per_second(self):
        return self.state.get_auto_clickers() / 3
    
    def add_passive_income(self):
        income = self.state.get_auto_clickers()
        if income > 0:
            self.add_coins(income)
    
    def reset(self) -> None:
        """Сброс игры"""
        self.state.set_coins(0)
        self.state.set_click_power(1)
        self.state.set_upgrades_bought(0)
        self.state.set_auto_clickers(0)
        self.save()