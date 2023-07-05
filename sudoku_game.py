from tkinter import  * 
from collections import Counter
import math
from data.sudoku_boards import board

root = Tk()

root.title('App')
root.geometry('381x287')
root.iconbitmap('logoicon.ico')

frame = LabelFrame(root, height = 209, width = 240, borderwidth = 4)
frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)

for i in range(3):
    for j in range(3):
        globals()[f'3x3_grid_{i * 3 + j}'] = LabelFrame(frame, borderwidth = 2, height = 70, width = 70)
        globals()[f'3x3_grid_{i * 3 + j}'].grid(row = i, column = j)

def highlight_field(e, j):
    global highlighted
    if board[j] != None: return
    e.widget['bg'] = 'aqua'
    for widget in highlighted:
        widget['widget']['bg'] = '#fff'
    highlighted = [{'widget': e.widget, 'i': j}]

def enter_number(i):
    if len(highlighted) == 0:
        return
    highlighted[-1]['widget']['text'] = i.char
    grid_check = check_for_3x3_grid(highlighted[-1])
    column_check = check_for_column(highlighted[-1])
    row_check = check_for_row(highlighted[-1])
    print(grid_check, column_check, row_check)
    if grid_check and row_check and column_check:
        complete_game()

def check_for_3x3_grid(d):
    i = d['i']
    elements = [item for item in range(81) if math.floor(item / 9) == math.floor(i / 9)]
    text_elements = [str(globals()[f'label_{i}']['text']) for i in elements]
    widget_elements = [globals()[f'label_{i}'] for i in elements]
    unique_elements = [item for item in list(dict(Counter(text_elements)).keys()) if item != '' and dict(Counter(text_elements))[item] == 1]
    for item in widget_elements:
        item['fg'] = 'red' if item['text'] != '' and str(item['text']) not in unique_elements else '#000'
    
    return len(unique_elements) == 9

def check_for_row(d):
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

def check_for_column(d):
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

def complete_game():
    global board
    print("Game completed!")
    # Reset the labels on the GUI
    for i in range(81):
        label = globals()[f'label_{i}']
        label['text'] = board[i] if board[i] is not None else ''
        label['fg'] = '#000'
        label['bg'] = '#ddd'

def bind_click_to_numbers():
    for grid_element in range(9):
        for i in range(3):
            for j in range(3):
                globals()[f'label_{grid_element * 9 + i * 3 + j}'] = \
                    Label(globals()[f'3x3_grid_{str(grid_element)}'], width = 2, borderwidth = 2, relief = GROOVE, text = board[grid_element * 9 + i * 3 + j]
                        if board[grid_element * 9 + i * 3 + j] is not None else '')
                globals()[f'label_{grid_element * 9 + i * 3 + j}'].grid(row = i, column = j)
                globals()[f'label_{grid_element * 9 + i * 3 + j}'].bind('<Button-1>', lambda e, k = grid_element * 9 + i * 3 + j: highlight_field(e, k))
                globals()[f'label_{grid_element * 9 + i * 3 + j}'].highlighted = False

bind_click_to_numbers()

highlighted = []

root.bind('<Escape>', lambda e: root.destroy())

for i in range(1, 10):
    root.bind(str(i), lambda i: enter_number(i))

if __name__ == '__main__':
    root.mainloop()
