import tkinter as tk
import os

def open_program():
    os.system('Python Katrina.py')
def open_program_n():
    os.system('Python MariaNikolaeva.py')


root = tk.Tk()
open_button = tk.Button(root, text='Открыть вариант Литвиновой', command=open_program)
open_button.pack(padx=20, pady=10)
open_button_n = tk.Button(root, text='Открыть вариант Николаевой', command=open_program_n)
open_button_n.pack(padx=20, pady=10)
root.mainloop()

