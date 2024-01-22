import tkinter as tk
from tkinter import Menu, messagebox, filedialog, ttk
from language import get_translation

class SettingsWindow(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Settings")
        self.parent = parent
    
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

class Alphard(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Alphard V 0.2")
        
        # Set the window size to 1920x1080 and maximize it
        self.geometry("1920x1080")
        self.state('zoomed')
        
        self.translation = get_translation()

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
        self.tree.heading("ipadr", text="IP Adress")
        self.tree.heading("tag", text="Tag")
        self.tree.heading("userpc", text="User@PC")
        self.tree.heading("version", text="Version")
        self.tree.heading("status", text="Status")
        self.tree.heading("userstatus", text="User Status")
        self.tree.heading("country", text="Country")
        self.tree.heading("os", text="Operating System")
        self.tree.heading("uptime", text="Uptime")

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
        about_text = "Alphard V 0.2\n\n"
        about_text += "Alphard is a simple tkinter-based application for managing remote Destops.\n"
        about_text += "Developed by Semaja Voye\n"
        about_text += "Contact Discord: letsplay\n"
        about_text += "GitHub: https://github.com/semajavoye/Alphard\n\n"
        about_text += "© 2024 Semaja Voyé. All rights reserved."

        messagebox.showinfo("About", about_text)


if __name__ == "__main__":
    app = Alphard()
    app.mainloop()