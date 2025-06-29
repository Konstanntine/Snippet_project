# -*- coding: utf-8 -*-
import tkinter as tk
import json
import os
import snippet_io
import tkinter.messagebox
import tkinter.simpledialog
import snippet_io

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        snippet_io.init_snippets_file()
        self.snippets = snippet_io.load_snippets()
        self.snippets.sort(key=lambda x: x['title'].lower())
        self.grid()
        self.create_widgets()
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.button_panel.grid(sticky="ns")

    def view_snippet(self, event):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            snippet = self.snippets[index]
        
            snippet_window = tk.Toplevel(self)
            snippet_window.title(snippet['title'])

            text = tk.Text(snippet_window, wrap="word")
            text.insert("1.0", snippet['code'])
            text.config(state="disabled")
            text.pack(padx=10, pady=10, fill="both", expand=True)

    def add_snippet(self):
        code = self.clipboard_get()
        title = tk.simpledialog.askstring("New Snippet", "Enter a title for the new snippet:")
        
        if title:
            new_snippet = {
                "title": title,
                "code": code,
                "language": "Python",
                "tags": [],
                "created": "2025-06-28"
            }

            self.snippets.sort(key=lambda x: x['title'].lower())
            self.snippets.append(new_snippet)
            snippet_io.save_snippets(self.snippets)
            self.refresh_listbox()

            tk.messagebox.showinfo("Saved!", f"Snippet '{title}' added.")
        else:
            tk.messagebox.showinfo("Cancelled", "No snippet was added.")

    def delete_snippet(self):
        index = self.listbox.curselection()[0]
        snippet_to_delete = self.displayed_snippets[index]

        confirm = tk.messagebox.askyesno("Confirm Delete", f"Delete '{snippet_to_delete['title']}'?")
        
        if confirm:
            self.snippets.remove(snippet_to_delete)
            snippet_io.save_snippets(self.snippets)
            self.refresh_listbox()
            
            tk.messagebox.showinfo("Deleted", f"Snippet '{snippet_to_delete['title']}' deleted.")

    def refresh_listbox(self):
        # A method that repopulates the listbox using self.displayed_snippets
        self.snippets.sort(key=lambda x: x['title'].lower())
        self.displayed_snippets = self.snippets.copy()

        self.listbox.delete(0, tk.END)
        for snippet in self.displayed_snippets:
            self.listbox.insert(tk.END, snippet["title"])
           
    def copy_snippet(self):
        selection = self.listbox.curselection()
        
        if selection:
            index = selection[0]
            snippet = snippet = self.displayed_snippets[index]
            self.clipboard_clear()
            self.clipboard_append(snippet["code"])
            
            tk.messagebox.showinfo("Copied!", f"'{snippet['title']}' copied to clipboard.")
        else:
            tk.messagebox.showwarning("No selection", "Please select a snippet first.")
  
    def create_widgets(self):
        self.listbox = tk.Listbox(self, width=50, height= 20)
        self.listbox.grid(row=0, column=0, rowspan=2, padx=10, pady=10, sticky="nsew")
        self.listbox.bind("<Double-Button-1>", self.view_snippet)
        self.refresh_listbox()


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