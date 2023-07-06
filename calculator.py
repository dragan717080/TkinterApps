import tkinter as tk
import parser
from base_app import BaseApp

class CalculatorApp(BaseApp):
    FONT_LARGE = ('Calibri', 12)
    FONT_MED = ('Calibri', 10)

    i = 0
    NEW_OPERATION = False

    def __init__(self):
        super().__init__()

        self.title('Calculator')
        self.resizable(width=False, height=False)

        for row in range(4):
            self.columnconfigure(row, pad=3)

        for column in range(5):
            self.rowconfigure(column, pad=3)

        self.display = tk.Entry(self, font=('Calibri', 13))
        self.display.grid(row=1, columnspan=6, padx=17, pady=10, sticky=tk.W + tk.E)

        self.init_ui()

    def init_ui(self):
        button_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

        for i, label in enumerate(button_labels):
            button = tk.Button(self, text=label, command=lambda num=i+1: self.get_variables(num), font=self.FONT_LARGE)
            button.grid(row=2 + i // 3, column=i % 3)

        operator_labels = [
            ('C', self.clear_all, 5, 0),
            ('0', lambda: self.get_variables(0), 5, 1),
            ('=', self.calculate, 5, 2),
            ('+', lambda: self.get_operation('+'), 2, 3),
            ('-', lambda: self.get_operation('-'), 3, 3),
            ('*', lambda: self.get_operation('*'), 4, 3),
            ('/', lambda: self.get_operation('/'), 5, 3),
            ('pi', lambda: self.get_operation('*3.14'), 2, 4),
            ('%', lambda: self.get_operation('%'), 3, 4),
            ('(', lambda: self.get_operation('('), 4, 4),
            ('exp', lambda: self.get_operation('**'), 5, 4),
            ('<-', self.undo, 2, 5),
            ('x!', lambda: self.factorial('!'), 3, 5),
            (')', lambda: self.get_operation(')'), 4, 5),
            ('^2', lambda: self.get_operation('**2'), 5, 5)
        ]

        for text, command, row, column in operator_labels:
            button = tk.Button(self, text=text, command=command, font=self.FONT_LARGE, foreground='red')
            button.grid(row=row, column=column, padx = (10, 0) if column == 0 else 0, pady = (0, 14) if row == 5 else 0)

    def factorial(self, operator):
        number = int(self.display.get())
        fact = 1
        try:
            while number > 0:
                fact = fact*number
                number -= 1
                self.clear_all()
                self.display.insert(0, fact)
        except Exception:
            self.clear_all()
            self.display.insert(0, 'Error')

    def clear_all(self, new_operation=True):
        self.display.delete(0, tk.END)
        self.NEW_OPERATION = new_operation

    def get_variables(self, num):
        if self.NEW_OPERATION:
            self.clear_all(new_operation=False)
        self.display.insert(self.i, num)
        self.i += 1

    def get_operation(self, operator):
        length = len(operator)
        self.display.insert(self.i, operator)
        self.i += length

    def undo(self):
        whole_string = self.display.get()
        if len(whole_string):
            self.clear_all(new_operation=False)
            self.display.insert(0, whole_string[:-1])
        else:
            self.clear_all()
            self.display.insert(0, 'Error, press AC')

    def calculate(self):
        whole_string = self.display.get()
        try:
            formulae = parser.expr(whole_string).compile()
            result = eval(formulae)
            self.clear_all()
            self.display.insert(0, result)
        except Exception:
            self.clear_all()
            self.display.insert(0, 'Error!')

app = CalculatorApp()
app.run()
