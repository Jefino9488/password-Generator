import random
import string
import tkinter as tk
from tkinter import IntVar
from tkinter import messagebox
import pyperclip


class PasswordGenerator:
    def __init__(self):
        pass

    @staticmethod
    def generate_password_logic(length, character_sets):
        password = ''
        for _ in range(length):
            character_set = random.choice(character_sets)
            password += random.choice(character_set)
        return password


class PasswordGeneratorUI:
    def __init__(self, node, generator):
        self.password_display = None
        self.root = node
        self.root.title("Password Generator")
        self.root.configure(bg='white')
        self.password_generator = generator
        self.length_var = IntVar()
        self.upper_var = IntVar()
        self.lower_var = IntVar()
        self.number_var = IntVar()
        self.special_var = IntVar()
        self.create_widgets()

    def create_widgets(self):
        length_label = tk.Label(self.root, text="Password Length:", bg='white')
        length_label.grid(row=0, column=0, columnspan=1, padx=10, pady=10)

        length_label = tk.Label(self.root, text="|", bg='white')
        length_label.grid(row=0, column=3, columnspan=1, padx=10, pady=10)

        length_slider = tk.Scale(self.root, from_=6, to=30, orient=tk.HORIZONTAL, length=150, variable=self.length_var, bg='white')
        length_slider.grid(row=0, column=1, padx=5, pady=5)

        length_label = tk.Label(self.root, text="|", bg='white')
        length_label.grid(row=1, column=3, columnspan=1, padx=10, pady=10)

        upper_check = tk.Checkbutton(self.root, text="Uppercase", variable=self.upper_var, bg='white')
        upper_check.grid(row=1, column=0, padx=20, pady=5, sticky=tk.W)

        lower_check = tk.Checkbutton(self.root, text="Lowercase", variable=self.lower_var, bg='white')
        lower_check.grid(row=2, column=0, padx=20, pady=5, sticky=tk.W)

        length_label = tk.Label(self.root, text="|", bg='white')
        length_label.grid(row=2, column=3, columnspan=1, padx=10, pady=10)

        number_check = tk.Checkbutton(self.root, text="Numbers", variable=self.number_var, bg='white')
        number_check.grid(row=3, column=0, padx=20, pady=5, sticky=tk.W)

        length_label = tk.Label(self.root, text="|", bg='white')
        length_label.grid(row=3, column=3, columnspan=1, padx=10, pady=10)

        special_check = tk.Checkbutton(self.root, text="Special Characters", variable=self.special_var, bg='white')
        special_check.grid(row=4, column=0, padx=20, pady=5, sticky=tk.W)

        length_label = tk.Label(self.root, text="|", bg='white')
        length_label.grid(row=4, column=3, columnspan=1, padx=10, pady=10)

        generate_button = tk.Button(self.root, text="Generate Password", command=self.generate_password, bg='orange',
                                    fg='white')
        generate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        length_label = tk.Label(self.root, text="|", bg='white')
        length_label.grid(row=5, column=3, columnspan=1, padx=10, pady=10)

        self.password_display = tk.Entry(self.root, width=30, state='readonly', font=('Courier', 12))
        self.password_display.grid(row=7, column=0, columnspan=2,padx=10, pady=10)

        copy_button = tk.Button(self.root, text="Copy to Clipboard", command=self.copy_to_clipboard, bg='blue',
                                fg='white')
        copy_button.grid(row=7, column=4, columnspan=1, padx=10, pady=10)

        length_label = tk.Label(self.root, text="_____________________________", bg='white')
        length_label.grid(row=6, column=0, padx=10, pady=0)
        length_label = tk.Label(self.root, text="_____________________________", bg='white')
        length_label.grid(row=6, column=1, padx=0, pady=0)
        length_label = tk.Label(self.root, text="_____", bg='white')
        length_label.grid(row=6, column=3, padx=0, pady=0)
        length_label = tk.Label(self.root, text="_____________________________", bg='white')
        length_label.grid(row=6, column=4, padx=0, pady=0)

        length_label = tk.Label(self.root, text="|", bg='white')
        length_label.grid(row=7, column=3, columnspan=1, padx=10, pady=10)

    def copy_to_clipboard(self):
        password = self.password_display.get()
        if password:
            pyperclip.copy(password)
            tk.messagebox.showinfo("Copy to Clipboard", "Password copied to clipboard!")

    def generate_password(self):
        length = int(self.length_var.get())
        character_sets = []

        if self.upper_var.get():
            character_sets.append(string.ascii_uppercase)
        if self.lower_var.get():
            character_sets.append(string.ascii_lowercase)
        if self.number_var.get():
            character_sets.append(string.digits)
        if self.special_var.get():
            character_sets.append('!@#$%^&*()-=_+[]{}|;:\'",.<>?/')

        if not character_sets:
            tk.messagebox.showwarning("Warning", "Please select at least one character set.")
            return

        password = self.password_generator.generate_password_logic(length, character_sets)

        self.password_display.config(state='normal')
        self.password_display.delete(0, tk.END)
        self.password_display.insert(0, password)
        self.password_display.config(state='readonly')


if __name__ == "__main__":
    root = tk.Tk()
    password_generator = PasswordGenerator()
    app = PasswordGeneratorUI(root, password_generator)
    root.mainloop()
