from tkinter import *
from tkinter import messagebox
import random



class Game_Window:
    background_colour = {
        '2': 'cyan',
        '4': 'blue',
        '8': 'forest green',
        '16': 'salmon',
        '32': 'purple3',
        '64': 'mint cream',
        '128': 'DarkOrange1',
        '256': 'PeachPuff2',
        '512': 'gold',
        '1024': 'DeepPink2',
        '2048': 'steel blue',
    }
    numbers_colour = {
        '2': 'grey1',
        '4': 'ghostwhite',
        '8': 'ghostwhite',
        '16': 'ghostwhite',
        '32': 'ghostwhite',
        '64': 'grey1',
        '128': 'ghostwhite',
        '256': 'ghostwhite',
        '512': 'grey1',
        '1024': 'grey1',
        '2048': 'ghostwhite',
    }

    def __init__(self):
        self.n = 4
        self.window = Tk()
        self.window.title('2048')
        self.gameArea = Frame(self.window, background='azure3')
        self.board = []
        self.gridCell = [[0] * 4 for i in range(4)]
        self.compress = False
        self.merge = False
        self.moved = False
        self.score = 0
        for i in range(4):
            rows = []
            for j in range(4):
                label = Label(self.gameArea, text='', background='azure4',font=('arial', 22, 'bold'), width=8, height=4)
                label.grid(row=i, column=j, padx=7, pady=7)
                rows.append(label);
            self.board.append(rows)
        self.gameArea.grid()


    def reverse(self):
        for ind in range(4):
            i = 0
            j = 3

            while (i < j):
                self.gridCell[ind][i], self.gridCell[ind][j] = self.gridCell[ind][j], self.gridCell[ind][i]
                i += 1
                j -= 1



    def transpose(self):
        self.gridCell = [list(t) for t in zip(*self.gridCell)]



    def compressGrid(self):
        self.compress = False
        temp = [[0] * 4 for i in range(4)]
        for i in range(4):
            cnt = 0
            for j in range(4):
                if self.gridCell[i][j] != 0:
                    temp[i][cnt] = self.gridCell[i][j]
                    if cnt != j:
                        self.compress = True
                    cnt += 1

        self.gridCell = temp



    def mergeGrid(self):
        self.merge = False
        for i in range(4):
            for j in range(4 - 1):
                if self.gridCell[i][j] == self.gridCell[i][j + 1] and self.gridCell[i][j] != 0:
                    self.gridCell[i][j] *= 2
                    self.gridCell[i][j + 1] = 0
                    self.score += self.gridCell[i][j]
                    self.merge = True



    def random_cell(self):
        cells = []
        for i in range(4):
            for j in range(4):
                if self.gridCell[i][j] == 0:
                    cells.append((i, j))

        curr = random.choice(cells)
        i = curr[0]
        j = curr[1]
        self.gridCell[i][j] = 2



    def can_merge(self):
        for i in range(4):
            for j in range(3):
                if self.gridCell[i][j] == self.gridCell[i][j + 1]:
                    return True

        for i in range(3):
            for j in range(4):
                if self.gridCell[i + 1][j] == self.gridCell[i][j]:
                    return True
        return False



    def paintGrid(self):
        for i in range(4):
            for j in range(4):
                if self.gridCell[i][j] == 0:
                    self.board[i][j].config(text='', background='azure4')
                else:
                    self.board[i][j].config(text=str(self.gridCell[i][j]),
                                            background=self.background_colour.get(str(self.gridCell[i][j])),
                                            fg=self.numbers_colour.get(str(self.gridCell[i][j])))


    def repaintGrid(self):
        self.n = 4
        self.window = Tk()
        self.window.title('2048')
        self.gameArea = Frame(self.window, background='azure3')
        self.board = []
        self.gridCell = [[0] * 4 for i in range(4)]
        self.compress = False
        self.merge = False
        self.moved = False
        self.score = 0
        for i in range(4):
            rows = []
            for j in range(4):
                label = Label(self.gameArea, text='', background='azure4', font=('arial', 22, 'bold'), width=8,
                              height=4)
                label.grid(row=i, column=j, padx=7, pady=7)
                rows.append(label);
            self.board.append(rows)
        self.gameArea.grid()

