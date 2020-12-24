from game_window import Game_Window
from game_actions import Game_Actions


if __name__ == '__main__':
    window = Game_Window()
    game = Game_Actions(window)
    game.start()