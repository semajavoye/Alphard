import tkinter as tk
from tkinter import Menu, messagebox, filedialog, ttk

class Alphard(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Alphard V 0.2")

        self.create_menu()
        self.create_table()

    def create_menu(self):
        menu_bar = Menu(self)
        self.config(menu=menu_bar)

        # File menu
        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # File menu subcategories
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_app)

        # Edit menu
        edit_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)

        # Edit menu subcategories
        edit_menu.add_command(label="Cut", command=self.cut)
        edit_menu.add_command(label="Copy", command=self.copy)
        edit_menu.add_command(label="Paste", command=self.paste)

        # Help menu
        help_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

    def create_table(self):
        # Create a Treeview widget
        self.tree = ttk.Treeview(self, columns=("Name", "Age", "Occupation"), show="headings")

        # Define column headings
        self.tree.heading("Name", text="Name")
        self.tree.heading("Age", text="Age")
        self.tree.heading("Occupation", text="Occupation")

        # Insert some sample data
        data = [("John Doe", 30, "Engineer"),
                ("Jane Smith", 25, "Teacher"),
                ("Bob Johnson", 35, "Doctor")]

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
        messagebox.showinfo("About", about_text)

if __name__ == "__main__":
    app = Alphard()
    app.mainloop()