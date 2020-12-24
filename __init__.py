from Game_Window import Game_Window
from Game_Actions import Game_Actions


if __name__ == '__main__':
    Game_Window = Game_Window()
    game = Game_Actions(Game_Window)
    game.start()