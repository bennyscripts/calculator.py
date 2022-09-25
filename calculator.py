import os
import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.create_widgets()

    def get_btn_width(self):
        return 5 if not os.name == "posix" else 2

    def create_num_grid(self):
        column = 0
        row = 1

        for i in reversed(range(9)):
            button = tk.Button(self, text=str(i + 1), width=self.get_btn_width(), height=2, command=lambda x=i + 1: self.add_to_screen(x))
            button.grid(column=column, row=row)

            column += 1
            if column == 3:
                column = 0
                row += 1

        button = tk.Button(self, text="0", width=self.get_btn_width(), height=2, command=lambda x=0: self.add_to_screen(x))
        button.grid(column=1, row=4)

    def create_operators_grid(self):
        column = 4
        row = 1
        operators = ["+", "-", "*", "/", "="]

        for operator in operators:
            if operator == "=":
                button = tk.Button(self, text=operator, width=self.get_btn_width(), height=2, command=self.calculate_screen)
            else:
                button = tk.Button(self, text=operator, width=self.get_btn_width(), height=2, command=lambda x=operator: self.add_to_screen(x))
            button.grid(column=column, row=row)

            row += 1

    def create_screen(self):
        self.screen = tk.Entry(self, borderwidth=0, justify="right")
        self.screen.grid(column=0, row=0, columnspan=5, ipady=10)

    def add_to_screen(self, value):
        self.screen.insert(tk.END, str(value) + "  ")
    
    def calculate_screen(self):
        result = eval(self.screen.get().strip().replace("  ", ""))
        self.screen.delete(0, tk.END)
        self.screen.insert(0, str(result) + "  ")

    def create_widgets(self):
        self.create_screen()
        self.create_num_grid()
        self.create_operators_grid()

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
