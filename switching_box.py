from tkinter import *

class App(object):

    def __init__(self, root):
        self.language = 'Python', 'Perl', 'C', 'Ruby', 'PHP', 'Java'

        self.leftbox = StringVar()
        self.leftbox.set(self.language)
        self.rightbox = StringVar()
        self.rightbox.set('')

        self.list_left = Listbox(root, listvariable=self.leftbox, width=16)
        self.list_left.pack(side=LEFT)
        self.list_right = Listbox(root, listvariable=self.rightbox)
        self.list_right.pack(side=RIGHT)

        self.frame = Frame(root)
        self.frame.pack(side=LEFT)
        Button(self.frame, text='->', command=self.move_to_right, width=7).pack(side=TOP)
        Button(self.frame, text='<-', command=self.move_to_left, width=7).pack(side=TOP)

    def move_to_right(self):
        if self.list_left.get(self.list_left.curselection()) != NONE:
            self.list_right.insert(END, self.list_left.get(self.list_left.curselection()))
            self.list_left.delete(self.list_left.curselection())

    def move_to_left(self):
        self.list_left.insert(END, self.list_right.get(self.list_right.curselection()))
        self.list_right.delete(self.list_right.curselection())

if __name__ == '__main__':
    root = Tk()
    app = App(root)
    root.mainloop()
