import tkinter as tk
from tkinter import filedialog, messagebox

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Untitled - Notepad")
        self.root.geometry("600x400")
        
        # Adding the text area
        self.text_area = tk.Text(self.root, undo=True)
        self.text_area.pack(expand=True, fill='both')
        
        # Creating the menu bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)
        
        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.quit_app)
        
        # Edit menu
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", command=self.text_area.edit_undo)
        self.edit_menu.add_command(label="Redo", command=self.text_area.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut", command=self.cut_text)
        self.edit_menu.add_command(label="Copy", command=self.copy_text)
        self.edit_menu.add_command(label="Paste", command=self.paste_text)
        
        # Help menu
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="About", command=self.show_about)
        
        # Adding a scrollbar
        self.scrollbar = tk.Scrollbar(self.text_area)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_area.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.text_area.yview)
        
        self.file_path = None

    def new_file(self):
        self.root.title("Untitled - Notepad")
        self.file_path = None
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        self.file_path = filedialog.askopenfilename(defaultextension=".txt",
                                                    filetypes=[("All Files", "*.*"),
                                                               ("Text Documents", "*.txt")])
        if self.file_path:
            self.root.title(f"{self.file_path} - Notepad")
            self.text_area.delete(1.0, tk.END)
            with open(self.file_path, "r") as file:
                self.text_area.insert(1.0, file.read())

    def save_file(self):
        if self.file_path:
            content = self.text_area.get(1.0, tk.END)
            with open(self.file_path, "w") as file:
                file.write(content)
        else:
            self.file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                          filetypes=[("All Files", "*.*"),
                                                                     ("Text Documents", "*.txt")])
            if self.file_path:
                self.root.title(f"{self.file_path} - Notepad")
                content = self.text_area.get(1.0, tk.END)
                with open(self.file_path, "w") as file:
                    file.write(content)

    def quit_app(self):
        self.root.quit()

    def cut_text(self):
        self.text_area.event_generate("<<Cut>>")

    def copy_text(self):
        self.text_area.event_generate("<<Copy>>")

    def paste_text(self):
        self.text_area.event_generate("<<Paste>>")

    def show_about(self):
        messagebox.showinfo("About Notepad", "A simple Notepad application using Python and Tkinter.")

if __name__ == "__main__":
    root = tk.Tk()
    notepad = Notepad(root)
    root.mainloop()
