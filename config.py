# config.py

# Пути
DATA_FILE = "data/save.json"

# Настройки окна
WINDOW_TITLE = "Кликер-игра"
WINDOW_SIZE = "400x500"

# Звук
SOUND_FREQ = 800
SOUND_DURATION = 100

# Настройки игры
START_COINS = 0
START_CLICK_POWER = 1

ACHIEVEMENTS = {
    "first_100": {"name": "Первые 100", "description": "Набрать 100 монет", "target": 100, "type": "coins"},
    "first_1000": {"name": "Тысячник", "description": "Набрать 1000 монет", "target": 1000, "type": "coins"},
    "first_upgrade": {"name": "Улучшайзер", "description": "Купить улучшение клика", "target": 1, "type": "upgrades"},
    "click_master": {"name": "Клик-мастер", "description": "Сделать 1000 кликов", "target": 1000, "type": "clicks"},
    "auto_lover": {"name": "Автолюбитель", "description": "Купить 5 автокликеров", "target": 5, "type": "auto_clickers"},
}