# views/main_window.py
import tkinter as tk
import winsound
from config import SOUND_FREQ, SOUND_DURATION, WINDOW_TITLE


class MainWindow:
    def __init__(self, controller):
        self.controller = controller
        self.window = tk.Tk()
        self.window.title(WINDOW_TITLE)
        self.window.geometry("400x500")
        self.window.resizable(False, False)
        
        self.create_widgets()
        self.update_display()
    
    def play_sound(self) -> None:
        """Проигрывает звук клика"""
        winsound.Beep(SOUND_FREQ, SOUND_DURATION)
    
    def update_display(self) -> None:
        """Обновляет отображение монет"""
        self.label.config(text=f"Монет: {self.controller.get_coins()}")
        self.label_power.config(text=f"Сила клика: {self.controller.get_click_power()}")
    
    def click(self) -> None:
        """Обычный клик"""
        self.play_sound()
        self.controller.add_coins(self.controller.get_click_power())
        self.update_display()
        self.label_warning.pack_forget()
    
    def add_custom(self) -> None:
        """Добавить из поля ввода"""
        try:
            value = int(self.entry.get())
            if value > 0:
                self.play_sound()
                self.controller.add_coins(value)
                self.update_display()
                self.entry.delete(0, tk.END)
                self.label_warning.pack_forget()
            else:
                self.label_warning.config(text="Введите положительное число!")
                self.label_warning.pack()
        except ValueError:
            self.label_warning.config(text="Введите число!")
            self.label_warning.pack()
    
    def reset(self) -> None:
        """Сброс игры"""
        self.play_sound()
        self.controller.reset()
        self.update_display()
        self.label_warning.pack_forget()
    
    def create_widgets(self) -> None:
        """Создаёт все виджеты"""
        # Поле ввода
        self.entry = tk.Entry(self.window, font=("Arial", 14))
        self.entry.pack(pady=10)
        
        # Кнопка добавления из поля
        btn_add_custom = tk.Button(
            self.window,
            text="Добавить монеты",
            command=self.add_custom,
            font=("Arial", 12),
            bg="orange"
        )
        btn_add_custom.pack(pady=5)
        
        # Кнопка обычного клика (большая)
        self.btn_click = tk.Button(
            self.window,
            text="КЛИК!",
            command=self.click,
            font=("Arial", 20, "bold"),
            bg="lightgreen",
            height=2,
            width=15
        )
        self.btn_click.pack(pady=20)
        
        # Отображение монет
        self.label = tk.Label(
            self.window,
            text=f"Монет: {self.controller.get_coins()}",
            font=("Arial", 16, "bold")
        )
        self.label.pack(pady=10)
        
        # Отображение силы клика
        self.label_power = tk.Label(
            self.window,
            text=f"Сила клика: {self.controller.get_click_power()}",
            font=("Arial", 12)
        )
        self.label_power.pack(pady=5)
        
        # Предупреждение
        self.label_warning = tk.Label(
            self.window,
            text="",
            fg="red",
            font=("Arial", 10)
        )
        
        # Кнопка сброса
        btn_reset = tk.Button(
            self.window,
            text="Сброс игры",
            command=self.reset,
            font=("Arial", 12),
            bg="lightcoral"
        )
        btn_reset.pack(pady=20)