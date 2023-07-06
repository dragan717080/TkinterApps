from tkinter import *
from PIL import ImageTk, Image
from db_models import Continent
from utils import Utils
from base_app import BaseApp

class EconomyStatsApp(BaseApp):
    def __init__(self):
        super().__init__()

        self.title('Continents economics stats')
        self.geometry('340x275')

    def append_labels(self):
        self.label = Label(self, image=image)
        self.label.pack(padx=19, pady=10)
        self.label.bind('<Button-1>', lambda e: self.get_continent_clicked(e))
        self.label_name = Label()
        self.label_name.pack(padx=21, anchor='center')
        self.label_name['text'] = 'Click on continent to get its indexes'
        self.label_fsi = Label()
        self.label_fei = Label()
        self.label_mspi = Label()
        self.label_ori = Label()

    def get_continent(self, x, y):
        coordinates = Utils.read_json_file('continents')
        for continent in coordinates:
            if coordinates[continent]['x_min'] <= x <= coordinates[continent]['x_max'] and \
                    coordinates[continent]['y_min'] <= y <= coordinates[continent]['y_max']:
                return continent

    def get_continent_clicked(self, e):
        continent = Continent.find(name=self.get_continent(e.x, e.y))
        if continent is None: return
        for i in range(1, 6):
            self.winfo_children()[i].pack(padx=21, anchor='w' if i > 1 else 'center')
        self.label_name['text'] = continent.name
        self.label_fsi['text'] = 'Fragile States Indexes ' + str(continent.fragile_states_index)
        self.label_fei['text'] = 'Factionalized Elites Indexes ' + str(continent.factionalized_elites_index)
        self.label_mspi['text'] = 'Military Spending Percentage Indexes ' + str(continent.military_spending_percentage_index)
        self.label_ori['text'] = 'Oil Reserves Indexes ' + str(continent.oil_reserves_index)

app = EconomyStatsApp()
image = ImageTk.PhotoImage(Image.open('assets/images/continents.jpg').resize((290, 140), Image.Resampling.LANCZOS))
app.append_labels()

if __name__ == '__main__':
    app.run()
