import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.create_widgets()

    def create_num_grid(self):
        column = 0
        row = 1

        for i in range(9):
            button = tk.Button(self, text=str(i + 1), width=5, height=2, command=lambda x=i + 1: self.add_to_screen(x))
            button.grid(column=column, row=row)

            column += 1
            if column == 3:
                column = 0
                row += 1

    def create_screen(self):
        self.screen = tk.Entry(self, borderwidth=0, justify="right")
        self.screen.grid(column=0, row=0, columnspan=3, ipady=10, ipadx=8)

    def add_to_screen(self, value):
        self.screen.insert(tk.END, value)

    def create_widgets(self):
        self.create_screen()
        self.create_num_grid()
        

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
