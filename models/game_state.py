# models/game_state.py

class GameState:
    def __init__(self):
        self.coins = 0
        self.click_power = 1
    
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