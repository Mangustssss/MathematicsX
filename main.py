import tkinter
from tkinter import ttk
import customtkinter
from PIL import Image, ImageTk



root_tk = tkinter.Tk()
root_tk.geometry("390x850")
root_tk.title("Mathematics X")
root_tk['background']='#363642'

# Center logo image
image_path = 'logo.png'
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

label = ttk.Label(image=photo)
label.pack()
label['background']='#363642'

label.place(relx=0.5, rely=0.5, anchor="center")

customtkinter.set_appearance_mode("Dark")


root_tk.mainloop()