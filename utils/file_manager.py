# utils/file_manager.py
import json
import os

def save_game(data: dict, filename: str) -> None:
    """Сохраняет данные игры в JSON файл"""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_game(filename: str) -> dict:
    """Загружает данные игры из JSON файла"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"coins": 0, "click_power": 1}