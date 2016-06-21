from tkinter import *


class App(object):
    def __init__(self, master):
        self.com = Button(master, text='Hello', command=self.say_hello)
        self.com.pack(side=BOTTOM)

    def say_hello(self):
        print('Hello')


root = Tk()
root.title('window with command')
root.geometry('800x400')

app = App(root)

root.mainloop()
