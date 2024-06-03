import tkinter as tk
from tkinter import filedialog, messagebox

class FileSearchView:
    def __init__(self, root, controller):
        self.controller = controller

        root.title("File and Folder Search")

        #directory entry and button
        self.frame_directory = tk.Frame(root)
        self.frame_directory.pack(padx=10, pady=5, fill=tk.X)
        self.label_directory = tk.Label(self.frame_directory, text="Directory:")
        self.label_directory.pack(side=tk.LEFT)
        self.entry_directory = tk.Entry(self.frame_directory, width=50)
        self.entry_directory.pack(side=tk.LEFT, padx=5)
        self.button_browse = tk.Button(self.frame_directory, text="Browse", command=self.controller.browse_directory)
        self.button_browse.pack(side=tk.LEFT)

        #pattern entry
        self.frame_pattern = tk.Frame(root)
        self.frame_pattern.pack(padx=10, pady=5, fill=tk.X)
        self.label_pattern = tk.Label(self.frame_pattern, text="Folder Name:")
        self.label_pattern.pack(side=tk.LEFT)
        self.entry_pattern = tk.Entry(self.frame_pattern, width=50)
        self.entry_pattern.pack(side=tk.LEFT, padx=5)

        #search button
        self.button_search = tk.Button(root, text="Search", command=self.controller.start_search)
        self.button_search.pack(pady=10)

        #listbox with a scrollbar
        self.frame_results = tk.Frame(root)
        self.frame_results.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        self.scrollbar = tk.Scrollbar(self.frame_results, orient=tk.VERTICAL)
        self.listbox_results = tk.Listbox(self.frame_results, yscrollcommand=self.scrollbar.set, width=80, height=20)
        self.scrollbar.config(command=self.listbox_results.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox_results.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def get_directory(self):
        return self.entry_directory.get()

    def set_directory(self, directory):
        self.entry_directory.delete(0, tk.END)
        self.entry_directory.insert(0, directory)

    def get_pattern(self):
        return self.entry_pattern.get()

    def show_results(self, results):
        self.listbox_results.delete(0, tk.END)
        for match in results:
            self.listbox_results.insert(tk.END, match)

    def show_warning(self, message):
        messagebox.showwarning("Input Error", message)
