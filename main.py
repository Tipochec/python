import tkinter as tk
import winsound

DATA_FILE = "data/click.txt"

class ClickerApp:
    def __init__(self) -> None:
        self.count = 0
        self.window = tk.Tk()
        self.window.title("Счётчик кликов")
        self.load_count()
        self.create_widgets()
    
    def load_count(self) -> None:
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                self.count = int(file.read())
        except (FileNotFoundError, ValueError):
            print("Не найден исполняемый файл")
    
    def save_count(self) -> None:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            file.write(str(self.count))

    def update_display(self) -> None:
        self.label.config(text=f"Счёт: {self.count}")
        self.label_warning.pack_forget()
    
    def add_count(self, value: int) -> None:
        self.count += value
        self.save_count()
        self.update_display()
        
    def add_from_entry(self)-> None:
        try:
            value = int(self.entry.get())
            self.add_count_with_sound(value)
            self.entry.delete(0, tk.END)
        except ValueError:
            self.label_warning.config(text="Введите число!")
            self.label_warning.pack()

    def play_sound(self):
        winsound.Beep(800, 100)

    def add_count_with_sound(self, value):
        self.play_sound()
        self.add_count(value)

    def plus1(self):
        self.add_count_with_sound(1)

    def plus5(self):
        self.add_count_with_sound(5)

    def minus1(self):
        if self.count > 0:
            self.add_count_with_sound(-1)
        else:
            self.label_warning.config(text="Нельзя спускаться ниже нуля")
            self.label_warning.pack()

    def reset(self):
        self.play_sound()
        self.count = 0
        self.save_count()
        self.update_display()
        
    def create_widgets(self)-> None:
        self.entry = tk.Entry(self.window)
        
        self.label = tk.Label(self.window, text=f"Счёт: {self.count}")
        self.label_warning = tk.Label(self.window, text="Нельзя спускатся ниже нуля")

        self.button_addClick = tk.Button(self.window, text=F"Добавить клики", command=self.add_from_entry)
        self.button_plusClick = tk.Button(self.window, text="Увеличь счётчик на 1", command=self.plus1)
        self.button_plus5Click = tk.Button(self.window, text="Увеличь счётчик на 5", command=self.plus5)
        self.button_minusClick = tk.Button(self.window, text="Уменьш счётчик на -1", command=self.minus1)
        self.button_null = tk.Button(self.window, text="Обнулить клики", command=self.reset)
        
        self.entry.pack()


        self.label_warning.pack_forget()
        self.label.pack()


        self.button_addClick.pack()
        self.button_plusClick.pack()
        self.button_plus5Click.pack()
        self.button_minusClick.pack()
        self.button_null.pack()



if __name__ == "__main__":
    app = ClickerApp()
    app.window.mainloop()
