from tkinter import *
from collections import Counter
import math
from data.sudoku_boards import get_board
from base_app import BaseApp

class SudokuApp(BaseApp):
    def __init__(self):
        super().__init__()
        self.title('Sudoku')
        self.geometry('381x287')

        self.frame = LabelFrame(self, height=209, width=240, borderwidth=4)
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.board = get_board()

        for i in range(3):
            for j in range(3):
                globals()[f'3x3_grid_{i * 3 + j}'] = LabelFrame(self.frame, borderwidth=2, height=70, width=70)
                globals()[f'3x3_grid_{i * 3 + j}'].grid(row=i, column=j)

        self.highlighted = []

        for i in range(1, 10):
            self.bind(str(i), lambda event, num=i: self.enter_number(event, num))

        self.bind_click_to_numbers()

    def highlight_field(self, event, j):
        if self.board[j] is not None:
            return

        event.widget['bg'] = 'aqua'
        for widget in self.highlighted:
            widget['widget']['bg'] = '#fff'
        self.highlighted = [{'widget': event.widget, 'i': j}]

    def enter_number(self, event, num):
        if len(self.highlighted) == 0:
            return
        self.highlighted[-1]['widget']['text'] = str(num)
        grid_check = self.check_for_3x3_grid(self.highlighted[-1])
        column_check = self.check_for_column(self.highlighted[-1])
        row_check = self.check_for_row(self.highlighted[-1])
        if grid_check and column_check and row_check:
            self.complete_game()

    def check_for_3x3_grid(self, d):
        i = d['i']
        elements = [item for item in range(81) if math.floor(item / 9) == math.floor(i / 9)]
        text_elements = [str(globals()[f'label_{i}']['text']) for i in elements]
        widget_elements = [globals()[f'label_{i}'] for i in elements]
        unique_elements = [item for item in list(dict(Counter(text_elements)).keys()) if item != '' and dict(Counter(text_elements))[item] == 1]
        for item in widget_elements:
            item['fg'] = 'red' if item['text'] != '' and str(item['text']) not in unique_elements else '#000'
        
        return len(unique_elements) == 9

    def check_for_row(self, d):
        i = d['i']
        row_beginnings = [i * 27 + j * 3 for i in range(3) for j in range(3)]
        rows = [[row_beginnings[row] + k + j * 9 for j in range(3) for k in range(3)] for row in range(9)]
        elements = [item for item in rows if i in item][0]
        text_elements = [str(globals()[f'label_{i}']['text']) for i in elements]
        widget_elements = [globals()[f'label_{i}'] for i in elements]
        unique_elements = [item for item in list(dict(Counter(text_elements)).keys()) if item != '' and dict(Counter(text_elements))[item] == 1]
        for item in widget_elements:
            item['fg'] = 'red' if item['text'] != '' and str(item['text']) not in unique_elements else '#000'
        
        return len(unique_elements) == 9

    def check_for_column(self, d):
        i = d['i']
        column_beginnings = [i * 9 + j for i in range(3) for j in range(3)]
        columns = [[column_beginnings[row] + k * 3 + j * 27 for j in range(3) for k in range(3)] for row in range(9)]
        elements = [item for item in columns if i in item][0]
        text_elements = [str(globals()[f'label_{i}']['text']) for i in elements]
        widget_elements = [globals()[f'label_{i}'] for i in elements]
        unique_elements = [item for item in list(dict(Counter(text_elements)).keys()) if item != '' and dict(Counter(text_elements))[item] == 1]
        for item in widget_elements:
            item['fg'] = 'red' if item['text'] != '' and str(item['text']) not in unique_elements else '#000'
        
        return len(unique_elements) == 9

    def complete_game(self):
        print('Game completed!')
        self.board = get_board()
        for i in range(81):
            label = globals()[f'label_{i}']
            label['text'] = self.board[i] if self.board[i] is not None else ''
            label['fg'] = '#000'
            label['bg'] = '#ddd'

    def bind_click_to_numbers(self):
        for grid_element in range(9):
            for i in range(3):
                for j in range(3):
                    globals()[f'label_{grid_element * 9 + i * 3 + j}'] = \
                        Label(globals()[f'3x3_grid_{str(grid_element)}'], width=2, borderwidth=2, relief=GROOVE,
                              text=self.board[grid_element * 9 + i * 3 + j]
                              if self.board[grid_element * 9 + i * 3 + j] is not None else '')
                    globals()[f'label_{grid_element * 9 + i * 3 + j}'].grid(row=i, column=j)
                    globals()[f'label_{grid_element * 9 + i * 3 + j}'].bind('<Button-1>',
                                                                          lambda e, k=grid_element * 9 + i * 3 + j: self.highlight_field(e, k))
                    globals()[f'label_{grid_element * 9 + i * 3 + j}'].highlighted = False

if __name__ == '__main__':
    app = SudokuApp()
    app.run()
