import tkinter
from tkinter import *
from tkinter import ttk
import customtkinter
from PIL import Image, ImageTk


root_tk = tkinter.Tk()

root_tk.geometry("390x850")
root_tk.title("Mathematics X")
root_tk['background']='#363642'

my_menu = Menu(root_tk)
root_tk.config(menu=my_menu)



# def menu():
#     print("[0] Option 1")
#     print("[1] Option 2")
#     print("[2] Option 3")

# menu()
# option = int(input("Enter your option: "))

# while option != 0:
#     if option == 1:
#         print("Option 1 has been called")
#     elif option == 2:
#         print("Option 2 has been called")
#     else:
#         print("Invalid option")

#     print()
#     menu()
#     option = int(input("Enter your option: "))


root_tk.mainloop()

