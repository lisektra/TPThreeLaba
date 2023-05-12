import tkinter as tk
import os

def open_program():
    os.system('python Katrina.py')

root = tk.Tk()
open_button = tk.Button(root, text='Открыть вариант Литвиновой', command=open_program)
open_button.pack(padx=20, pady=10)
root.mainloop()
