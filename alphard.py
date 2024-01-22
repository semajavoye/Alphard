import tkinter as tk
from tkinter import Menu, messagebox, filedialog, ttk
import json
from language import get_translation, get_languages, get_settinglanguage

def get_version():
    with open("settings.json", "r") as f:
        settings = json.load(f)
        version = settings["version"]
    return version

class SettingsWindow(tk.Toplevel):
    def __init__(self, parent):
        self.translation = get_translation()
        
        tk.Toplevel.__init__(self, parent)
        self.title(self.translation["file_menu"]["settings"])
        
        self.geometry("680x560")
        self.create_menu()
        
        self.parent = parent
        
    def create_menu(self):
        settingslabel = tk.Label(self, text=self.translation["file_menu"]["settings"])
        settingslabel.pack()

        # Create a StringVar to store the selected language
        selected_language = tk.StringVar()

        # Get the available languages
        available_languages = get_languages()
        
        dropdown = tk.OptionMenu(self, selected_language, *available_languages)
        dropdown.pack()

        # Set the default language based on the current setting
        selected_language.set(get_settinglanguage())

class Alphard(tk.Tk):
    def __init__(self):
        self.translation = get_translation()
        
        tk.Tk.__init__(self)
        self.title(self.translation["alphard"] + ' ' + get_version())
        
        # maximize the window
        self.state('zoomed')
        

        self.create_menu()
        self.create_table()

    def create_menu(self):
        menu_bar = Menu(self)
        self.config(menu=menu_bar)

        # File menu
        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label=self.translation["file_menu"]["file"], menu=file_menu)

        # File menu subcategories
        file_menu.add_command(label=self.translation["file_menu"]["new"], command=self.new_file)
        file_menu.add_command(label=self.translation["file_menu"]["open"], command=self.open_file)
        file_menu.add_command(label=self.translation["file_menu"]["save"], command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label=self.translation["file_menu"]["settings"], command=self.settings)
        file_menu.add_command(label=self.translation["file_menu"]["exit"], command=self.exit_app)

        # Edit menu
        edit_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label=self.translation["edit_menu"]["edit"], menu=edit_menu)

        # Edit menu subcategories
        edit_menu.add_command(label=self.translation["edit_menu"]["cut"], command=self.cut)
        edit_menu.add_command(label=self.translation["edit_menu"]["copy"], command=self.copy)
        edit_menu.add_command(label=self.translation["edit_menu"]["paste"], command=self.paste)

        # Help menu
        help_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label=self.translation["help_menu"]["help"], menu=help_menu)
        help_menu.add_command(label=self.translation["help_menu"]["about"], command=self.show_about)

    def create_table(self):
        # Create a Treeview widget
        self.tree = ttk.Treeview(self, columns=("ipadr", "tag", "userpc", "version", "status", "userstatus", "country", "os", "uptime"), show="headings")


        # Define column headings
        self.tree.heading("ipadr", text=self.translation["tree"]["ipadr"])
        self.tree.heading("tag", text=self.translation["tree"]["tag"])
        self.tree.heading("userpc", text=self.translation["tree"]["userpc"])
        self.tree.heading("version", text=self.translation["tree"]["version"])
        self.tree.heading("status", text=self.translation["tree"]["status"])
        self.tree.heading("userstatus", text=self.translation["tree"]["userstatus"])
        self.tree.heading("country", text=self.translation["tree"]["country"])
        self.tree.heading("os", text=self.translation["tree"]["os"])
        self.tree.heading("uptime", text=self.translation["tree"]["uptime"])

        # Insert some sample data
        data = []

        for item in data:
            self.tree.insert("", "end", values=item)

        # Pack the Treeview widget
        self.tree.pack(pady=20)

    def new_file(self):
        messagebox.showinfo("New", "Creating a new file")

    def open_file(self):
        file_path = filedialog.askopenfilename(title="Open File", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            messagebox.showinfo("Open", f"Opening file: {file_path}")

    def save_file(self):
        file_path = filedialog.asksaveasfilename(title="Save File", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            messagebox.showinfo("Save", f"Saving file to: {file_path}")
            
    def settings(self):
        settings_window = SettingsWindow(self)
        

    def exit_app(self):
        if messagebox.askyesno("Exit", "Do you really want to exit?"):
            self.destroy()

    # Additional methods for Edit menu
    def cut(self):
        messagebox.showinfo("Edit", "Cutting selected text")

    def copy(self):
        messagebox.showinfo("Edit", "Copying selected text")

    def paste(self):
        messagebox.showinfo("Edit", "Pasting clipboard content")

    def show_about(self):
        about_text = self.translation["dialogs"]["about"]   

        messagebox.showinfo(self.translation["dialogs"]["aboutlabel"], about_text)


if __name__ == "__main__":
    app = Alphard()
    app.mainloop()