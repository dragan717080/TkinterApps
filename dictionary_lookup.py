from tkinter import *
import requests
from dotenv import dotenv_values
from playsound import playsound
import re
from PIL import ImageTk, Image, ImageDraw
from base_app import BaseApp

class DictionaryLookupApp(BaseApp):
    def __init__(self):
        super().__init__()
        self.URL = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'
        self.API_KEY = dotenv_values('.env')['MERRIAM-WEBSTER_API_KEY']

        self.geometry('391x239')
        self.title('Dictionary Lookup App')

        self.draw_image('label_audio.jpg')
        self.image = ImageTk.PhotoImage((Image.open('label_audio.jpg').resize((40, 40), Image.Resampling.LANCZOS)))

        self.search_text = StringVar()
        self.search_text.trace('w', lambda name, index, mode, text=self.search_text: self.get_search(self.search_text))

        self.search = Entry(self, textvariable=self.search_text)
        self.search.pack(pady=19)

        self.label_audio = Label(self, image=self.image)
        self.label_audio.bind('<Button-1>', lambda e: playsound(e.widget.sound_file))

        labels = [
            ('name', {'font': ('Helvetica', 16, 'bold')}),
            ('phonetic', None),
            ('meaning', None),
            ('functional', None),
            ('stems', None)
        ]

        for label_name, params in labels:
            label = Label(self, **params) if params else Label(self)
            setattr(self, f'label_{label_name}', label)
            label.pack()

    def draw_image(self, output_path):
        image = Image.new('RGB', (140, 140), '#fff')
        draw = ImageDraw.Draw(image)
        draw.polygon([(24, 19), (24, 127), (122, 73)], fill='#000')
        image.save(output_path)

    def get_search(self, text):
        text.set(re.sub('[^A-Za-z]', '', text.get()))
        if len(text.get()) > 0:
            response = requests.get(f'{self.URL}{text.get()}?key={self.API_KEY}').json()
            self.get_label_for_correct(response[0]) if len(response) > 0 and 'meta' in response[0] else self.get_label_for_fail()

    def get_label_for_correct(self, data):
        audio_file = self.get_audio_file(data)
        data['meta']['id'] = data['meta']['id'].split(':')[0]
        self.label_name['text'] = data['meta']['id']
        self.label_functional['text'] = data['fl']
        self.label_stems['text'] = ', '.join(data['meta']['stems'])
        meaning_text = ''
        self.label_meaning['text'] = ''
        for item in data['def'][0]['sseq']:
            meaning_text = self.get_meaning(item[0][1], meaning_text) if type(item[0][1]) == dict else self.get_meaning(item[0][1][0][1], meaning_text)
        self.label_meaning['text'] += meaning_text
        self.label_audio.pack_forget() if audio_file is None else self.label_audio.pack()
        self.label_audio.sound_file = audio_file

    def get_meaning(self, d, meaning_text):
        meanings = list(d.keys())
        meaning = d[meanings[1]] if len(meanings) > 1 else d[meanings[0]]
        if type(meaning) == list and meaning[0][0] == 'text':
            meaning = re.sub(r'{bc}|{it}|{/it}', '', meaning[0][1])
            meaning_text += meaning + '\n'
        elif type(meaning) == dict and 'dt' in meaning:
            meaning_text += re.sub(r'{bc}|{it}|{/it}', '', meaning['dt'][0][1]) + '\n'
        return meaning_text

    def get_audio_file(self, data):
        try:
            audio = data['hwi']['prs'][0]['sound']['audio']
            return f'https://media.merriam-webster.com/audio/prons/en/us/mp3/{audio[0]}/{audio}.mp3'
        except Exception:
            return None

    def run(self):
        self.mainloop()

app = DictionaryLookupApp()
app.run()
