# views/main_window.py
import customtkinter as ctk
import pygame
from config import WINDOW_TITLE

# Настройка темы
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class MainWindow:
    def __init__(self, controller):
        self.controller = controller
        
        # Инициализация звука
        pygame.mixer.init()
        try:
            self.click_sound = pygame.mixer.Sound("assets/sounds/click.wav")
            self.buy_sound = pygame.mixer.Sound("assets/sounds/applepay.wav")
        except:
            print('Звук не найден')
            self.click_sound = None
            self.buy_sound = None
        
        # Создаём окно
        self.window = ctk.CTk()
        self.window.title(WINDOW_TITLE)
        self.window.geometry("500x700")
        self.window.resizable(False, False)
        
        self.create_widgets()
        self.update_display()
        self.start_passive_timer()
        
    def play_sound_buy(self):
        if self.buy_sound:
            self.buy_sound.play()
    
    def play_sound(self) -> None:
        """Проигрывает звук клика"""
        if self.click_sound:
            self.click_sound.play()
            
    def buy_crit_upgrade(self):
        if self.controller.buy_crit_upgrade():
            self.play_sound_buy()
            self.update_display()
            self.label_warning.configure(text="")
        else:
            self.label_warning.configure(text="Не хватает монет!")
    
    def update_display(self) -> None:
        self.label.configure(text=f"Монет: {self.controller.get_coins()}")
        self.label_power.configure(text=f"Сила клика: {self.controller.get_click_power()}")

        self.btn_crit.configure(text=f"Улучшить крит (+5%) ({self.controller.get_crit_upgrade_cost()} монет)")
        self.label_crit.configure(text=f"Крит-шанс: {self.controller.get_crit_chance()}% (x{self.controller.get_crit_multiplier()})")
        
        # Обновляем кнопку улучшения клика
        self.btn_upgrade.configure(text=f"Улучшить клик ({self.controller.get_upgrade_cost()} монет)")
        
        # Обновляем кнопку автокликера
        self.btn_auto.configure(text=f"Купить автокликер ({self.controller.get_auto_clicker_cost()} монет)")
        
        # Обновляем информацию об автокликерах
        auto_count = self.controller.state.get_auto_clickers()
        income = self.controller.get_passive_income_per_second()
        self.label_auto.configure(text=f"Автокликеры: {auto_count} | Доход: {income:.1f} монет/сек")
    
    def click(self):
        self.play_sound()
        gain, is_crit = self.controller.click()
        
        # Если был крит — показываем всплывающее сообщение
        if is_crit:
            self.label_warning.configure(text=f"КРИТИЧЕСКИЙ КЛИК! +{gain} монет!", text_color="gold")
            self.window.after(1500, lambda: self.label_warning.configure(text="", text_color="red"))
        
        self.update_display()
    
    def add_custom(self) -> None:
        """Добавить из поля ввода"""
        try:
            value = int(self.entry.get())
            if value > 0:
                self.play_sound()
                self.controller.add_coins(value)
                self.update_display()
                self.entry.delete(0, ctk.END)
                self.label_warning.configure(text="")
            else:
                self.label_warning.configure(text="Введите положительное число!")
        except ValueError:
            self.label_warning.configure(text="Введите число!")
    
    def reset(self) -> None:
        """Сброс игры"""
        self.play_sound()
        self.controller.reset()
        self.update_display()
        self.label_warning.configure(text="")
    
    def buy_upgrade(self):
        if self.controller.buy_click_upgrade():
            self.play_sound_buy()
            self.update_display()
            self.label_warning.configure(text="")
        else:
            self.label_warning.configure(text="Не хватает монет!")
    
    def buy_auto_clicker(self) -> None:
        if self.controller.buy_auto_clicker():
            self.play_sound_buy()
            self.update_display()
            self.label_warning.configure(text="")
        else:
            self.label_warning.configure(text="Не хватает монет!")

    def start_passive_timer(self):
        self.controller.add_passive_income()
        self.update_display() 
        self.window.after(3000, self.start_passive_timer)
    
    def create_widgets(self) -> None:
        """Создаёт все виджеты"""
        
        # Поле ввода
        self.entry = ctk.CTkEntry(
            self.window,
            placeholder_text="Введите количество монет",
            width=250,
            font=("Arial", 14)
        )
        self.entry.pack(pady=10)
        
        # Кнопка добавления из поля
        btn_add_custom = ctk.CTkButton(
            self.window,
            text="Добавить монеты",
            command=self.add_custom,
            width=250,
            fg_color="orange",
            hover_color="darkorange"
        )
        btn_add_custom.pack(pady=5)
        
        # Кнопка обычного клика (большая)
        self.btn_click = ctk.CTkButton(
            self.window,
            text="КЛИК!",
            command=self.click,
            width=280,
            height=80,
            font=("Arial", 24, "bold"),
            fg_color="green",
            hover_color="darkgreen"
        )
        self.btn_click.pack(pady=20)
        
        # Отображение монет
        self.label = ctk.CTkLabel(
            self.window,
            text=f"Монет: {self.controller.get_coins()}",
            font=("Arial", 20, "bold")
        )
        self.label.pack(pady=10)
        
        # Отображение силы клика
        self.label_power = ctk.CTkLabel(
            self.window,
            text=f"Сила клика: {self.controller.get_click_power()}",
            font=("Arial", 14)
        )
        self.label_power.pack(pady=5)
        
        # Кнопка покупки улучшения
        self.btn_upgrade = ctk.CTkButton(
            self.window,
            text=f"Улучшить клик ({self.controller.get_upgrade_cost()} монет)",
            command=self.buy_upgrade,
            width=280,
            fg_color="gold",
            text_color="black",
            hover_color="orange"
        )
        self.btn_upgrade.pack(pady=5)
        
        # Отображение крит-шанса
        self.label_crit = ctk.CTkLabel(
            self.window,
            text=f"Крит-шанс: {self.controller.get_crit_chance()}% (x{self.controller.get_crit_multiplier()})",
            font=("Arial", 12)
        )
        self.label_crit.pack(pady=5)

        # Кнопка улучшения крита
        self.btn_crit = ctk.CTkButton(
            self.window,
            text=f"Улучшить крит (+5%) ({self.controller.get_crit_upgrade_cost()} монет)",
            command=self.buy_crit_upgrade,
            width=280,
            fg_color="purple",
            hover_color="darkviolet"
        )
        self.btn_crit.pack(pady=5)
        
        # Кнопка покупки автокликера
        self.btn_auto = ctk.CTkButton(
            self.window,
            text=f"Купить автокликер ({self.controller.get_auto_clicker_cost()} монет)",
            command=self.buy_auto_clicker,
            width=280,
            fg_color="lightblue",
            text_color="black",
            hover_color="skyblue"
        )
        self.btn_auto.pack(pady=5)
        
        # Отображение количества автокликеров и дохода
        self.label_auto = ctk.CTkLabel(
            self.window,
            text=f"Автокликеры: 0 | Доход: 0 монет/сек",
            font=("Arial", 12)
        )
        self.label_auto.pack(pady=5)
        
        # Предупреждение
        self.label_warning = ctk.CTkLabel(
            self.window,
            text="",
            text_color="red",
            font=("Arial", 12)
        )
        self.label_warning.pack(pady=5)
        
        # Кнопка сброса
        btn_reset = ctk.CTkButton(
            self.window,
            text="Сброс игры",
            command=self.reset,
            width=250,
            fg_color="red",
            hover_color="darkred"
        )
        btn_reset.pack(pady=20)