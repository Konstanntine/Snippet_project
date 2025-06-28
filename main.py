import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)



    def add_snippet(self):
        pass
    def delete_snippet(self):
        pass
    def add_to_clipboard(self):
        pass


    def create_widgets(self):
        self.right_panel = tk.Frame(self)
        self.right_panel.grid(row=0, column=2, rowspan=2, sticky='nsew')
        self.listbox = tk.Listbox(self.right_panel, width=40, height=15)
        self.listbox.pack(fill='both', expand=True, padx=10, pady=10)
        self.add = tk.Button(self, text='Add', command = self.add_snippet)
        self.add.grid(row=0, column=1)
        self.quitButton = tk.Button(self, text='Quit',command=self.quit)
        self.quitButton.grid(row=1, column=1)
        self.add = tk.Button(self, text='Delete', command = self.delete_snippet)
        self.add.grid(row=2, column=1)
        self.add = tk.Button(self, text='Copy', command = self.add_to_clipboard)
        self.add.grid(row=3, column=1, sticky='ew')


if __name__ == "__main__":
    app = Application()
    app.master.geometry('600x400')
    app.master.title('snippet_storage')
    app.mainloop()   