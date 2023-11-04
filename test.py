import tkinter as tk
from tkinter import ttk

class SampleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multi-Page App")

        self.pages = {}
        self.create_page("Page 1", "This is Page 1")
        self.create_page("Page 2", "This is Page 2")
        self.create_page("Page 3", "This is Page 3")

        self.current_page = None

        self.show_page("Page 1")

    def create_page(self, page_name, content):
        frame = ttk.Frame(self.root)
        label = ttk.Label(frame, text=content)
        label.pack(padx=10, pady=10)
        self.pages[page_name] = (frame, label)

    def show_page(self, page_name):
        if self.current_page:
            self.pages[self.current_page][0].pack_forget()
        self.pages[page_name][0].pack()
        self.current_page = page_name

if __name__ == "__main__":
    root = tk.Tk()
    app = SampleApp(root)
    root.mainloop()