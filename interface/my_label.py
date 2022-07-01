from tkinter.ttk import Label

from constants import *


class MyLabel(Label):
    def __init__(self, master, text="Title", font=LABEL_FONT, fg=FG_COLOR, bg=BG_COLOR, justify="left", width=None,
                 relief=None):
        super().__init__(master=master, text=text, justify=justify, foreground=fg, background=bg, font=font,
                         width=width, relief=relief)

    def updateText(self, text):
        self.config(text=text)

    def position(self, x, y, height=CONST_HEIGHT, width=LABEL_WIDTH, anchor=INPUT_ANCHOR):
        self.place(x=x, y=y, height=height, width=width, anchor=anchor)
