# models/game_state.py

class GameState:
    def __init__(self):
        self.coins = 0
        self.click_power = 1
        self.cost_upgrate = 50
        self.upgrades_bought = 0
        self.auto_clickers = 0
    
    def add_coins(self, amount: int) -> None:
        self.coins += amount
    
    def get_coins(self) -> int:
        return self.coins
    
    def set_coins(self, value: int) -> None:
        self.coins = value
    
    
    
    def get_click_power(self) -> int:
        return self.click_power
    
    def set_click_power(self, value: int) -> None:
        self.click_power = value
        
    
    
    def get_upgrades_bought(self) -> int:
        return self.upgrades_bought
    
    def add_upgrade(self):
        self.upgrades_bought += 1
    
    def set_upgrades_bought(self, value: int):
        self.upgrades_bought = value
    
    
    
    def get_auto_clickers(self) -> int:
        return self.auto_clickers
    
    def add_auto_clicker(self):
        self.auto_clickers += 1
    
    def set_auto_clickers(self, value: int) -> None:
        self.auto_clickers = value