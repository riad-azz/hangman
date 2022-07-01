from os import path
from random import choice
from tkinter import Tk, messagebox, Label, PhotoImage
from tkinter.ttk import Separator

import pyglet

from constants import *
from interface.my_button import MyButton
from interface.my_input import MyInput
from interface.my_label import MyLabel


class MyApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        # -- App Settings --
        self['bg'] = BG_COLOR
        self.title('Hangman')
        self.resizable(False, False)
        self.geometry(f"{WIDTH}x{HEIGHT}")
        pyglet.font.add_file('./assets/fonts/Vollkorn-Bold.ttf')
        self.iconbitmap('./assets/app_icon.ico')
        # -- Game Vars --
        self.words = self.load_words()
        self.images = self.load_images()
        self.tries = 6
        self.tried_letters = None
        self.wrong_letters = []
        self.wrong_index = 0
        self.word = None
        self.display_word = None
        self.answer_word = None
        # -- App Widgets --
        # Title
        self.l_wrong_letters = MyLabel(self, text='Wrong letters : ', font=LABEL_FONT)
        self.l_wrong_letters.position(x=170, y=40)
        Separator(self, orient='horizontal').place(relx=0, y=80, height=2, relwidth=1)
        # Wrong letters
        l_wrong_x = 380
        for i in range(self.tries):
            temp = MyLabel(self, text='', fg='red', font=WRONG_FONT, )
            temp.position(x=l_wrong_x, y=40, anchor='w')
            self.wrong_letters.append(temp)
            l_wrong_x += 80
        # Hangman Image
        self.image = Label(self, bg=BG_COLOR)
        self.image.place(x=(WIDTH / 2), y=300, anchor='center')
        # Word
        Separator(self, orient='horizontal').place(relx=0, y=530, height=2, relwidth=1)
        self.l_word = MyLabel(self, text='', font=WORD_FONT)
        self.l_word.position(x=(WIDTH / 2), y=580)
        Separator(self, orient='horizontal').place(relx=0, y=630, height=2, relwidth=1)
        # User Input
        self.e_answer = MyInput(self)
        self.e_answer.bind('<Return>', self.check_answer)
        self.e_answer.position(x=(WIDTH / 2), y=680, height=60, width=200)
        self.b_confirm = MyButton(self, text='Confirm', command=self.check_answer)
        self.b_confirm.position(x=(WIDTH / 2), y=750, width=200)

        # Start the game
        self.start_game()

    @staticmethod
    def load_words():
        # Default words
        words = ['jackpot', 'video', 'lucky', 'luxury', 'awkward', 'capture', 'funny', 'correct']
        if path.exists('words.txt'):
            with open('words.txt', 'r') as f:
                try:
                    data = f.read().split('\n')
                    if len(data) >= 1:
                        words = data
                except Exception as e:
                    messagebox.showerror("Error", f"Error loading word.txt file\n{e}")
                    quit()
        else:
            messagebox.showinfo("Info", f"Loading failed word.txt file.\nwords set to default")

        return words

    @staticmethod
    def load_images():
        temp = []

        for i in range(7):
            try:
                image = PhotoImage(file=f'./assets/images/hanger_{i}.png')
                temp.append(image)
            except:
                messagebox.showerror("Error", "Failed to load game images")
        try:
            image = PhotoImage(file=f'./assets/images/win.png')
            temp.append(image)
        except:
            messagebox.showerror("Error", "Failed to load game images")

        if len(temp) != 8:
            quit()
        return temp

    def start_game(self):
        self.image.configure(image=self.images[0])
        self.word = choice(self.words)
        self.tries = 6
        self.tried_letters = []
        self.wrong_index = 0
        for label in self.wrong_letters:
            label.configure(text='_')
        self.display_word = ['_'] * len(self.word)
        self.update_word()
        self.answer_word = ""

    def update_word(self):
        display_word = " ".join(self.display_word).upper()
        self.l_word.configure(text=display_word)

    def check_answer(self, event=None):
        answer = self.e_answer.get().lower()

        if len(answer) != 1:
            messagebox.showerror('Error', "Answer field can't be empty")
            return
        elif answer in self.tried_letters:
            messagebox.showerror('Error', f"You already used the letter {answer.upper()}")
            return

        if answer in self.word:
            self.correct_answer(answer)
        else:
            self.wrong_answer(answer)

        # Clear input
        self.e_answer.delete(0, 'end')

        # Check game state
        self.check_game()

    def correct_answer(self, letter):
        self.tried_letters.append(letter)
        for i, x in enumerate(self.word):
            if x == letter:
                self.display_word[i] = x
        self.answer_word = "".join(self.display_word)
        self.update_word()

    def wrong_answer(self, letter):
        self.tried_letters.append(letter)
        self.wrong_letters[self.wrong_index].configure(text=letter.upper())
        self.wrong_index += 1
        self.tries -= 1
        self.image.configure(image=self.images[self.wrong_index])

    def check_game(self):
        if self.tries == 0:
            messagebox.showerror('Lost', "YOU LOST !!")
            self.start_game()

        if self.answer_word == self.word:
            self.image.configure(image=self.images[-1])
            messagebox.showinfo('WIN', "YOU WON !!")
            self.start_game()
