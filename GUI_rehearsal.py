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
        help_string1 = '(W)Up (S)Down (A)Left (D)Right'
        help_string2 = '    (R)Restart (Q)Exit'
        gameover_string = '         GAME OVER'
        win_string = '          YOU WIN!'

        self.value11.delete(0)
        self.value11.insert(END, self.field[0][0])
        self.value12.delete(0)
        self.value12.insert(END, self.field[0][1])
        self.value13.delete(0)
        self.value13.insert(END, self.field[0][2])
        self.value14.delete(0)
        self.value14.insert(END, self.field[0][3])
        self.value21.delete(0)
        self.value21.insert(END, self.field[1][0])
        self.value22.delete(0)
        self.value22.insert(END, self.field[1][1])
        self.value23.delete(0)
        self.value23.insert(END, self.field[1][2])
        self.value24.delete(0)
        self.value24.insert(END, self.field[1][3])
        self.value31.delete(0)
        self.value31.insert(END, self.field[2][0])
        self.value32.delete(0)
        self.value32.insert(END, self.field[2][1])
        self.value33.delete(0)
        self.value33.insert(END, self.field[2][2])
        self.value34.delete(0)
        self.value34.insert(END, self.field[2][3])
        self.value41.delete(0)
        self.value41.insert(END, self.field[3][0])
        self.value42.delete(0)
        self.value42.insert(END, self.field[3][1])
        self.value43.delete(0)
        self.value43.insert(END, self.field[3][2])
        self.value44.delete(0)
        self.value44.insert(END, self.field[3][3])

        if self.is_win():
            print(win_string)
        else:
            if self.is_gameover():
                print(gameover_string)
            else:
                print(help_string1)
        print(help_string2)


def main():
    def init():
        game_field.reset()
        return 'Game'

    def not_game(state):
        game_field.draw()
        action = get_user_action()
        responses = defaultdict(lambda: state)
        responses['Restart'], responses['Exit'] = 'Init', 'Exit'
        return responses[action]

    def game():
        game_field.draw(stdscr)
        action = get_user_action(stdscr)
        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'
        if game_field.move(action):
            if game_field.is_win():
                return 'Win'
            if game_field.is_gameover():
                return 'Gameover'
        return 'Game'

    state_actions = {
        'Init': init,
        'Win': lambda: not_game('Win'),
        'Gameover': lambda: not_game('Gameover'),
        'Game': game
    }
    print("haha")
    # console.use_default_color()
    game_field = GameField(win=32)

    state = 'Init'

    while state != 'Exit':
        state = state_actions[state]()


if __name__ == '__main__':
    root = Tk()
    root.geometry('400x300')
    app = App(root)
    root.mainloop()
