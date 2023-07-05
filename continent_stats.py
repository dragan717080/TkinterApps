from tkinter import *
from PIL import ImageTk, Image
from db_models import Continent
from utils import Utils

class App(Tk):
    def __init__(self):
        super().__init__()

        self.title('Continents economics indexes')
        self.geometry('340x275')
        self.iconbitmap("logoicon.ico")
        self.add_exit_shortcut()

    def append_labels(self):
        self.label = Label(self, image=image)
        self.label.pack(padx=19, pady=10)
        self.label.bind('<Button-1>', lambda e: get_continent_clicked(e))
        self.label_name = Label()
        self.label_fsi = Label()
        self.label_fei = Label()
        self.label_mspi = Label()
        self.label_ori = Label()

    def add_exit_shortcut(self):
        self.bind('<Escape>', lambda e: self.destroy())

app = App()
image = ImageTk.PhotoImage(Image.open('assets/images/continents.jpg').resize((290, 140), Image.Resampling.LANCZOS))
app.append_labels()
app.label_name.pack(padx=21, anchor='center')
app.label_name['text'] = 'Click on continent to get its indexes'

def get_continent(x, y):
    coordinates = Utils.read_json_file('continents.json')
    for continent in coordinates:
        if coordinates[continent]['x_min'] <= x <= coordinates[continent]['x_max'] and \
            coordinates[continent]['y_min'] <= y <= coordinates[continent]['y_max']:
                return continent

def get_continent_clicked(e):
    continent = Continent.find(name=get_continent(e.x, e.y))
    if continent is not None:
        for i in range(1, 6):
            app.winfo_children()[i].pack(padx=21, anchor='w' if i > 1 else 'center')
        app.label_name['text'] = continent.name
        app.label_fsi['text'] = 'Fragile States Indexes ' + str(continent.fragile_states_index)
        app.label_fei['text'] = 'Factionalized Elites Indexes ' + str(continent.factionalized_elites_index)
        app.label_mspi['text'] = 'Military Spending Percentage Indexes ' + str(continent.military_spending_percentage_index)
        app.label_ori['text'] = 'Oil Reserves Indexes ' + str(continent.oil_reserves_index)

if __name__ == '__main__':
    app.mainloop()
