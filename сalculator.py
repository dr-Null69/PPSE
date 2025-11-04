import tkinter as tk
from tkinter import messagebox

class CalculatorApp:

    def __init__(self, master):
        self.master = master
        master.title("Простий Калькулятор")
        master.geometry("350x120")
        master.resizable(False, False)


        self.entry_input = tk.Entry(
            master, 
            width=30, 
            font=('Arial', 16), 
            justify='right',
            relief=tk.SUNKEN,
            bd=3
        )
        self.entry_input.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
        
        self.entry_input.bind('<Return>', lambda event: self.calculate())

        self.calculate_button = tk.Button(
            master, 
            text="Обчислити", 
            command=self.calculate,
            font=('Arial', 14, 'bold'),
            bg="#3a3a3",       
            activebackground="#45a049"
        )
        self.calculate_button.grid(row=1, column=0, padx=10, pady=5, columnspan=2, sticky="we")

    def calculate(self):
        """
        дописати логіку обчислення виразу з поля введення
        і відображення результату або помилки.
        """
    def show_error(self, e):
        """
        дописати логіку відображення повідомлення про помилку
        """

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()