# views/main_window.py
import tkinter as tk
import pygame
from config import WINDOW_TITLE


class MainWindow:
    def __init__(self, controller):
        self.controller = controller
        pygame.mixer.init()
        try:
            self.click_sound = pygame.mixer.Sound("assets/sounds/click.wav")
        except:
            print('Звук не найден')
            self.click_sound = None
        self.window = tk.Tk()
        self.window.title(WINDOW_TITLE)
        self.window.geometry("400x500")
        self.window.resizable(False, False)
        
        self.create_widgets()
        self.update_display()
        self.start_passive_timer()
    
    def play_sound(self) -> None:
        """Проигрывает звук клика"""
        if self.click_sound:
            self.click_sound.play()
    
    def update_display(self) -> None:
        self.label.config(text=f"Монет: {self.controller.get_coins()}")
        self.label_power.config(text=f"Сила клика: {self.controller.get_click_power()}")
        
        # Обновляем кнопку улучшения клика
        self.btn_upgrade.config(text=f"Улучшить клик ({self.controller.get_upgrade_cost()} монет)")
        
        # Обновляем кнопку автокликера
        self.btn_auto.config(text=f"Купить автокликер ({self.controller.get_auto_clicker_cost()} монет)")
        
        # Обновляем информацию об автокликерах
        auto_count = self.controller.state.get_auto_clickers()
        income = self.controller.get_passive_income_per_second()
        self.label_auto.config(text=f"Автокликеры: {auto_count} | Доход: {income:.1f} монет/сек")
    
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
        
    def buy_upgrade(self):
        if self.controller.buy_click_upgrade(50):
            self.update_display()
            self.label_warning.pack_forget()
        else:
            self.label_warning.config(text="Не хватает монет!")
            self.label_warning.pack()
    
    def buy_auto_clicker(self) -> None:
        if self.controller.buy_auto_clicker():
            self.update_display()
            self.label_warning.pack_forget()
        else:
            self.label_warning.config(text="Не хватает монет!")
            self.label_warning.pack()

    def start_passive_timer(self):
        self.controller.add_passive_income()
        self.update_display() 
        self.window.after(3000, self.start_passive_timer)
        
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
        
        # Кнопка покупки улучшения
        self.btn_upgrade = tk.Button(
            self.window,
            text=f"Улучшить клик ({self.controller.get_upgrade_cost()} монет)",
            command=self.buy_upgrade,
            font=("Arial", 12),
            bg="gold"
        )
        self.btn_upgrade.pack(pady=5)
        
        # Кнопка покупки автокликера
        self.btn_auto = tk.Button(
            self.window,
            text=f"Купить автокликер ({self.controller.get_auto_clicker_cost()} монет)",
            command=self.buy_auto_clicker,
            font=("Arial", 12),
            bg="lightblue"
        )
        self.btn_auto.pack(pady=5)
        
        # Отображение количества автокликеров и дохода
        self.label_auto = tk.Label(
            self.window,
            text=f"Автокликеры: 0 | Доход: 0 монет/сек",
            font=("Arial", 10)
        )
        self.label_auto.pack(pady=5)
        
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