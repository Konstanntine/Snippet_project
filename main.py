import tkinter as tk
import json
import os
import snippet_io
from snippet_io import init_snippets_file
# Initialize the snippets file if it doesn't exist

def load_snippets(filename="snippets.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_snippets(snippets, filename="snippets.json"):
    with open(filename, "w") as f:
        json.dump(snippets, f, indent=4)

# -*- coding: utf-8 -*-
#
class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.button_panel.grid(sticky="ns")
        snippet_io.init_snippets_file()
    def load_snippets(filename="snippets.json"):
        try:
            with open(filename, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
    def save_snippets(snippets, filename="snippets.json"):
        with open(filename, "w") as f:
            json.dump(snippets, f, indent=4)




    def add_snippet(self):
        pass
    def delete_snippet(self):
        pass
    def copy_snippet(self):
        pass
        


    def create_widgets(self):
        self.listbox = tk.Listbox(self, width=50, height= 20)
        self.listbox.grid(row=0, column=0, rowspan=2, padx=10, pady=10, sticky="nsew")
        
        self.button_panel = tk.Frame(self)
        self.button_panel.grid(row=0, column=1, rowspan=2, sticky="ns", padx=5, pady=10)
        
        self.addbutton = tk.Button(self.button_panel, width=10, text='Add', command=self.add_snippet)
        self.addbutton.pack(pady=(0, 5))

        self.copybutton = tk.Button(self.button_panel, width=10, text='Copy', command=self.copy_snippet)
        self.copybutton.pack(pady=(0, 5))

        self.deletebutton = tk.Button(self.button_panel, width=10, text='Delete', command=self.delete_snippet)
        self.deletebutton.pack(pady=(0, 5))

        self.quitButton = tk.Button(self.button_panel, width=10, text='Quit', command=self.quit)
        self.quitButton.pack(pady=(0, 5))





if __name__ == "__main__":
    app = Application()
    app.master.geometry('600x400')
    app.master.title('snippet_storage')
    app.mainloop()   