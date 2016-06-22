from tkinter import *

from random import randrange, choice

from collections import defaultdict


class App(object):

    def __init__(self, root):

        self.left_frame = Frame(root, borderwidth=4, relief='groove')
        self.left_frame.pack(side=LEFT)
        self.right_frame = Frame(root, borderwidth=4, relief='groove')
        self.right_frame.pack(side=RIGHT)

        self.row1 = Frame(self.left_frame)
        self.row1.pack(side=TOP)
        self.row2 = Frame(self.left_frame)
        self.row2.pack(side=TOP)
        self.row3 = Frame(self.left_frame)
        self.row3.pack(side=TOP)
        self.row4 = Frame(self.left_frame)
        self.row4.pack(side=TOP)

        self.value11 = Text(self.row1, relief='groove', width=6, height=3)
        self.value11.pack(side=LEFT)
        self.value12 = Text(self.row1, relief='groove', width=6, height=3)
        self.value12.pack(side=LEFT)
        self.value13 = Text(self.row1, relief='groove', width=6, height=3)
        self.value13.pack(side=LEFT)
        self.value14 = Text(self.row1, relief='groove', width=6, height=3)
        self.value14.pack(side=LEFT)

        self.value21 = Text(self.row2, relief='groove', width=6, height=3)
        self.value21.pack(side=LEFT)
        self.value22 = Text(self.row2, relief='groove', width=6, height=3)
        self.value22.pack(side=LEFT)
        self.value23 = Text(self.row2, relief='groove', width=6, height=3)
        self.value23.pack(side=LEFT)
        self.value24 = Text(self.row2, relief='groove', width=6, height=3)
        self.value24.pack(side=LEFT)

        self.value31 = Text(self.row3, relief='groove', width=6, height=3)
        self.value31.pack(side=LEFT)
        self.value32 = Text(self.row3, relief='groove', width=6, height=3)
        self.value32.pack(side=LEFT)
        self.value33 = Text(self.row3, relief='groove', width=6, height=3)
        self.value33.pack(side=LEFT)
        self.value34 = Text(self.row3, relief='groove', width=6, height=3)
        self.value34.pack(side=LEFT)

        self.value41 = Text(self.row4, relief='groove', width=6, height=3)
        self.value41.pack(side=LEFT)
        self.value42 = Text(self.row4, relief='groove', width=6, height=3)
        self.value42.pack(side=LEFT)
        self.value43 = Text(self.row4, relief='groove', width=6, height=3)
        self.value43.pack(side=LEFT)
        self.value44 = Text(self.row4, relief='groove', width=6, height=3)
        self.value44.pack(side=LEFT)

        self.button_row1 = Frame(self.right_frame)
        self.button_row1.pack(side=TOP)
        self.button_row2 = Frame(self.right_frame)
        self.button_row2.pack(side=TOP)
        self.button_row3 = Frame(self.right_frame)
        self.button_row3.pack(side=TOP)
        self.button_row4 = Frame(self.right_frame)
        self.button_row4.pack(side=TOP)

        self.button1 = Button(self.button_row1, text='Up', width=9, height=2).pack()
        self.button2 = Button(self.button_row2, text='Left', width=9, height=2).pack(side=LEFT)
        self.button3 = Button(self.button_row2, text='Right', width=9, height=2).pack(side=LEFT)
        self.button4 = Button(self.button_row3, text='Down', width=9, height=2).pack()
        self.button5 = Button(self.button_row4, text='Reset', width=9, height=2, bg='yellow').pack(side=LEFT)
        self.button6 = Button(self.button_row4, text='Exit', width=9, height=2, bg='red').pack(side=LEFT)

        self.height = 4
        self.width = 4
        self.win_value = 2048
        self.score = 0
        self.high_score = 0
        self.field = [[0 for i in range(self.width)] for j in range(self.height)]
        self.reset()

    def spawn(self):
        if randrange(100) > 89:
            new_element = 4
        else:
            new_element = 2
        (i, j) = choice([(i, j) for i in range(self.width) for j in range(self.height) if self.field[i][j] == 0])
        self.field[i][j] = new_element

    def reset(self):
        if self.score > self.high_score:
               self.high_score = self.score
        self.score = 0
        self.field = [[0 for i in range(self.width)] for j in range(self.height)]
        self.spawn()

        # command = self.move('Up')


if __name__ == '__main__':
    root = Tk()
    root.geometry('400x300')
    app = App(root)
    root.mainloop()
