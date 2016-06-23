from tkinter import *

from random import randrange, choice

from collections import defaultdict

actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']


def transpose(field):
    return [list(row) for row in zip(*field)]


def invert(field):
    return [row[::-1] for row in field]


class App(object):
    def __init__(self, root):

        self.height = 4
        self.width = 4
        self.win_value = 2048
        self.score = 0
        self.high_score = 0
        self.field = [[0 for i in range(self.width)] for j in range(self.height)]

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

        self.button1 = Button(self.button_row1, text='Up', width=9, height=2, command=self.respond('Up')).pack()
        self.button2 = Button(self.button_row2, text='Left', width=9, height=2, command=self.respond('Left')).pack(
            side=LEFT)
        self.button3 = Button(self.button_row2, text='Right', width=9, height=2, command=self.respond('Right')).pack(
            side=LEFT)
        self.button4 = Button(self.button_row3, text='Down', width=9, height=2, command=self.respond('Down')).pack()
        self.button5 = Button(self.button_row4, text='Reset', width=9, height=2, command=self.respond('Reset'),
                              bg='yellow').pack()

        self.reset()

    def spawn(self):
        new_element = 2
        if randrange(100) > 89:
            new_element = 4
        (i, j) = choice([(i, j) for i in range(self.width) for j in range(self.height) if self.field[i][j] == 0])
        self.field[i][j] = new_element

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.field = [[0 for i in range(self.width)] for j in range(self.height)]
        self.spawn()

    def move_is_possible(self, direction):
        def row_is_left_movable(row):
            def change(i):
                if row[i] == 0 and row[i + 1] != 0:
                    return True
                if row[i] != 0 and row[i + 1] == row[i]:
                    return True
                return False

            return any(change(i) for i in range(len(row) - 1))

        check = {}
        check['Left'] = lambda field: any(row_is_left_movable(row) for row in field)
        check['Right'] = lambda field: any(row_is_left_movable(row) for row in field)
        check['Up'] = lambda field: check['Left'](transpose(field))
        check['Down'] = lambda field: check['Right'](transpose(field))

        if direction in check:
            return check[direction](self.field)
        else:
            return False

    def respond(self, action):
        print(action)
        if action == 'Restart':
            self.reset()
        else:
            if self.move(action):
                self.draw()

    def is_win(self):
        return any(any(i >= self.win_value for i in row) for row in self.field)

    def is_gameover(self):
        return not any(self.move_is_possible(move) for move in actions)

    def move(self, direction):
        def move_row_left(row):
            def tighten(row):
                new_row = [i for i in row if i != 0]
                new_row += [0 for i in range(len(row) - len(new_row))]
                return new_row

            def merge(row):
                pair = False
                new_row = []
                for i in range(len(row)):
                    if pair:
                        new_row.append(2 * row[i])
                        self.score += 2 * row[i]
                        pair = False
                    else:
                        if i + 1 < len(row) and row[i] == row[i + 1]:
                            pair = True
                            new_row.append(0)
                        else:
                            new_row.append(row[i])
                assert len(new_row) == len(row)
                return new_row

            return tighten(merge(tighten(row)))

        moves = {}
        moves['Left'] = lambda field: [move_row_left(row) for row in field]
        moves['Right'] = lambda field: invert(moves['Left'](invert(field)))
        moves['Up'] = lambda field: transpose(moves['Left'](transpose(field)))
        moves['Down'] = lambda field: transpose(moves['Right'](transpose(field)))

        if direction in moves:
            if self.move_is_possible(direction):
                self.field = moves[direction](self.field)
                self.spawn()
                return True
            else:
                return False

    def draw(self):
        game_over_string = '         GAME OVER'
        win_string = '          YOU WIN!'

        self.value11.delete("1.0", END)
        self.value11.insert(END, self.field[0][0])
        self.value12.delete("1.0", END)
        self.value12.insert(END, self.field[0][1])
        self.value13.delete("1.0", END)
        self.value13.insert(END, self.field[0][2])
        self.value14.delete("1.0", END)
        self.value14.insert(END, self.field[0][3])
        self.value21.delete("1.0", END)
        self.value21.insert(END, self.field[1][0])
        self.value22.delete("1.0", END)
        self.value22.insert(END, self.field[1][1])
        self.value23.delete("1.0", END)
        self.value23.insert(END, self.field[1][2])
        self.value24.delete("1.0", END)
        self.value24.insert(END, self.field[1][3])
        self.value31.delete("1.0", END)
        self.value31.insert(END, self.field[2][0])
        self.value32.delete("1.0", END)
        self.value32.insert(END, self.field[2][1])
        self.value33.delete("1.0", END)
        self.value33.insert(END, self.field[2][2])
        self.value34.delete("1.0", END)
        self.value34.insert(END, self.field[2][3])
        self.value41.delete("1.0", END)
        self.value41.insert(END, self.field[3][0])
        self.value42.delete("1.0", END)
        self.value42.insert(END, self.field[3][1])
        self.value43.delete("1.0", END)
        self.value43.insert(END, self.field[3][2])
        self.value44.delete("1.0", END)
        self.value44.insert(END, self.field[3][3])

        if self.is_win():
            print(win_string)
        elif self.is_gameover():
            print(game_over_string)


if __name__ == '__main__':
    root = Tk()
    root.geometry('400x300')
    app = App(root)
    root.mainloop()
