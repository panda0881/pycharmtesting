from tkinter import *


class App(object):
    def __init__(self, root):
        self.text = Text(root, relief='groove', width=6, height=3)
        self.text.pack()
        self.button = Button(root, text='Left', width=9, height=2, command=self.go).pack(side=LEFT)

    def go(self):
        print('go')
        self.text.delete("1.0", END)
        self.text.insert(END, 1)


if __name__ == '__main__':
    root = Tk()
    root.geometry('400x300')
    app = App(root)
    root.mainloop()
