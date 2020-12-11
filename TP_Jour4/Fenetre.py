from tkinter import *


class Application(Tk):

    def __init__(self):
        Tk.__init__(self)

        self.create_menu_top()

        self.geometry('300x200')
        self.title('Orchestra')

    def create_menu_top(self):
        menu_master = Menu(self)
        menu_file = Menu(menu_master, tearoff=0)
        menu_file.add_command(label='New', command=self.do_something)
        menu_file.add_command(label='Open', command=self.do_something)
        menu_file.add_command(label='Save', command=self.do_something)
        menu_file.add_separator()
        menu_file.add_command(label='Exit', command=self.quit)
        menu_master.add_cascade(label='File', menu=menu_file)

        menu_edit = Menu(menu_master, tearoff=0)
        menu_edit.add_command(label='Copy', command=self.do_something)
        menu_edit.add_command(label='Paste', command=self.do_something)
        menu_edit.add_command(label='Undo', command=self.do_something)
        menu_master.add_cascade(label='Edit', menu=menu_edit)

        self.config(menu=menu_master)

    @staticmethod
    def do_something():
        print('something')


window = Application()
window.mainloop()