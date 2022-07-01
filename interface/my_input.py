from string import ascii_letters
from tkinter import StringVar
from tkinter.ttk import Entry, Style

from constants import *


class MyInput(Entry):
    def __init__(self, master, fg=FG_INPUT, bg=BG_INPUT, font=INPUT_FONT, hint=""):
        self.var = StringVar()
        self.validate_command = (master.register(self.validate), '%P')
        super().__init__(master, foreground=fg, background=bg, font=font, textvariable=self.var,
                         width=3, justify="center", validate='key', validatecommand=self.validate_command)
        self.delete(0, 'end')
        self.insert(0, hint)

    def position(self, x, y, height=CONST_HEIGHT, width=INPUT_WIDTH, anchor=INPUT_ANCHOR):
        self.place(x=x, y=y, height=height, width=width, anchor=anchor)

    @staticmethod
    def validate(value):
        if len(value) <= 1:
            if value in ascii_letters or value == '':
                return True
            else:
                return False
        else:
            return False
