from tkinter import *
from tkinter import messagebox
from Game_Window import Game_Window
import pyglet
import random


class Game_Actions:

    def __init__(self, gamepanel):
        self.gamepanel = gamepanel
        self.end = False
        self.won = False


    def start(self):
        print("Game Starting: \n")
        self.gamepanel.random_cell()
        self.gamepanel.random_cell()
        self.gamepanel.paintGrid()
        self.gamepanel.window.bind('<Key>', self.link_keys)
        self.gamepanel.window.mainloop()


    def link_keys(self, event):
        if self.end or self.won:
            return

        self.gamepanel.compress = False
        self.gamepanel.merge = False
        self.gamepanel.moved = False
        presed_key = event.keysym

        if presed_key == 'Up':
            self.gamepanel.transpose()
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()
            self.gamepanel.transpose()

        elif presed_key == 'Down':
            self.gamepanel.transpose()
            self.gamepanel.reverse()
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()
            self.gamepanel.reverse()
            self.gamepanel.transpose()

        elif presed_key == 'Left':
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()

        elif presed_key == 'Right':
            self.gamepanel.reverse()
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()
            self.gamepanel.reverse()

        else:
            pass

        self.gamepanel.paintGrid()
        print(f"Total score: {self.gamepanel.score}")
        flag = 0

        for i in range(4):
            for j in range(4):
                if (self.gamepanel.gridCell[i][j] == 4):
                    flag = 1
                    break

        if (flag == 1):  # user reached 2048
            self.won = True
            self.finished_game(flag)
            print("\nGame finished: User Won")
            if self.play_again() == True:
                game = Game_Window()
                self.__init__(game)
                self.start()
            return


        for i in range(4):
            for j in range(4):
                if self.gamepanel.gridCell[i][j] == 0:
                    flag = 1
                    break

        if not (flag or self.gamepanel.can_merge()):
            self.end = True
            self.finished_game(flag)
            print("\nGame finished: User Lost")
            if self.play_again() == False:
                sys.exit("Thanks for playing!")

        if self.gamepanel.moved:
            self.gamepanel.random_cell()

        self.gamepanel.paintGrid()


    def finished_game(self, flag):
        if flag == 1:   # win animation
            animation = pyglet.image.load_animation('images/win.gif')
        else:           # loss animation
            animation = pyglet.image.load_animation('images/game_over.gif')
        animSprite = pyglet.sprite.Sprite(animation)
        w = animSprite.width
        h = animSprite.height
        window = pyglet.window.Window(width=w, height=h/1.3)
        r, g, b, alpha = 0.5, 0.5, 0.8, 0.5
        pyglet.gl.glClearColor(r, g, b, alpha)
        @window.event
        def on_draw():
            window.clear()
            animSprite.draw()
        pyglet.app.run()

    def play_again(self):
        title = "Play Again"
        message = "Would you like to play again?"
        return messagebox.askyesno(title, message)




