from tkinter import *


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

        self.value11 = Message(self.row1, relief='groove')
        self.value11.pack(side=LEFT)
        self.value12 = Message(self.row1, relief='groove')
        self.value12.pack(side=LEFT)
        self.value13 = Message(self.row1, relief='groove')
        self.value13.pack(side=LEFT)
        self.value14 = Message(self.row1, relief='groove')
        self.value14.pack(side=LEFT)

        self.value21 = Message(self.row2, relief='groove')
        self.value21.pack(side=LEFT)
        self.value22 = Message(self.row2, relief='groove')
        self.value22.pack(side=LEFT)
        self.value23 = Message(self.row2, relief='groove')
        self.value23.pack(side=LEFT)
        self.value24 = Message(self.row2, relief='groove')
        self.value24.pack(side=LEFT)

        self.value31 = Message(self.row3, relief='groove')
        self.value31.pack(side=LEFT)
        self.value32 = Message(self.row3, relief='groove')
        self.value32.pack(side=LEFT)
        self.value33 = Message(self.row3, relief='groove')
        self.value33.pack(side=LEFT)
        self.value34 = Message(self.row3, relief='groove')
        self.value34.pack(side=LEFT)

        self.value41 = Message(self.row4, relief='groove')
        self.value41.pack(side=LEFT)
        self.value42 = Message(self.row4, relief='groove')
        self.value42.pack(side=LEFT)
        self.value43 = Message(self.row4, relief='groove')
        self.value43.pack(side=LEFT)
        self.value44 = Message(self.row4, relief='groove')
        self.value44.pack(side=LEFT)

        self.button_row1 = Frame(self.right_frame)
        self.button_row1.pack(side=TOP)
        self.button_row2 = Frame(self.right_frame)
        self.button_row2.pack(side=TOP)
        self.button_row3 = Frame(self.right_frame)
        self.button_row3.pack(side=TOP)
        self.button_row4 = Frame(self.right_frame)
        self.button_row4.pack(side=TOP)

        self.button1 = Button(self.button_row1, text='Up', width=7).pack()
        self.button2 = Button(self.button_row2, text='Left', width=7).pack(side=LEFT)
        self.button3 = Button(self.button_row2, text='Right', width=7).pack(side=LEFT)
        self.button4 = Button(self.button_row3, text='Down', width=7).pack()
        self.button5 = Button(self.button_row4, text='Reset', bg='yellow', width=7).pack(side=LEFT)
        self.button6 = Button(self.button_row4, text='Exit', bg='red', width=7).pack(side=LEFT)

        # command = self.move('Up')


if __name__ == '__main__':
    root = Tk()
    # root.geometry('400x400')
    app = App(root)
    root.mainloop()
