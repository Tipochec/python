# main.py
from controllers.game_controller import GameController
from views.main_window import MainWindow

if __name__ == "__main__":
    controller = GameController()
    app = MainWindow(controller)
    app.window.mainloop()