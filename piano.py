import pygame
from tkinter import *
from utils import Utils
from base_app import BaseApp

class PianoApp(BaseApp):
    FONT = ('Calibri', 10)
    
    def __init__(self):
        super().__init__()
        self.title('PianoApp')
        self.geometry('791x251')
        self.resizable(width=False, height=False)

        pygame.mixer.init()

        self.data = Utils.read_json_file('keys')
        self.keyboard_sounds = self.data['sounds']

        self.frame = Frame(self, width=740, height=210, bg='#000')
        self.frame.place(relx=0.05, rely=0.1)

        self.WHITE_KEYS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
        self.BLACK_KEYS = ['!', '@', '$', '%', '^', '*', '(', 'Q', 'W', 'E', 'T', 'Y', 'I', 'O', 'P', 'S', 'D', 'G', 'H', 'J', 'L', 'Z', 'C', 'V', 'B']
        self.BLACK_KEY_INDEXES = [0, 1, 3, 4, 5, 7, 8, 10, 11, 12, 14, 15, 17, 18, 19, 21, 22, 24, 25, 26, 28, 29, 31, 32, 33]

        self.bind_keys()
        self.create_key_buttons()

        self.mainloop()

    def play_sound(self, sound_file):
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()

    def clicked_key(self, key):
        try:
            sound_file = f'data/keys_mp3/{self.keyboard_sounds[key]}.mp3'
            self.play_sound(sound_file)
        except KeyError:
            print(f'No sound found for key {key}')
        except pygame.error:
            print('Error playing sound')

    def bind_keys(self):
        for key in self.WHITE_KEYS + self.BLACK_KEYS:
            self.bind(f'<{key}>', lambda event, key=key: self.clicked_key(key))

    def create_key_buttons(self):
        for i, key in enumerate(self.WHITE_KEYS):
            self.create_key_button(key, 7 + 20 * i, 10, 2, 17, '#fff', '#000', pady=34)

        for i, key in enumerate(self.BLACK_KEYS):
            distance = 19 + 20 * self.BLACK_KEY_INDEXES[i]
            self.create_key_button(key, distance, 2, 1, 7, '#000', '#fff')

    def create_key_button(self, key, x, y, width, height, bg_color, fg_color, padx=0, pady=0):
        params = {
            'width': width, 'height': height, 'text': key, 'bg': bg_color, 'fg': fg_color, 'padx': padx, 'pady': pady, 
            'command': lambda: self.clicked_key(key), 'font': self.FONT
        }
        button = Button(self.frame, **params)
        button.place(x=x, y=y)
        return button

    def unbind_keys(self):
        for key in self.WHITE_KEYS + self.BLACK_KEYS:
            self.unbind(f'<{key}>')

app = PianoApp()
PianoApp.run()

