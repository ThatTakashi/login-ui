# Fantasy roleplaying game
# By Takashi
# Version 0.1
# 21/01/23

import customtkinter
import tkinter as tk
from tkinter import *
import time
import random
from PIL import Image, ImageTk
from splashtext import splash

# Set global application background color
background = '#333538'

# Setup the main tkinter window
root = customtkinter.CTk()
root.geometry('700x480')
root.resizable(False, False)
root.configure(fg_color=background)
root.title("Login/Sign up")

# Load the application icon
ico = Image.open('icon.png')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

# Set themes for CustomTkinter
customtkinter.set_appearance_mode("Dark")  # Modes: "Dark" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")

# Load the login background image
image = Image.open("login.png")
img = ImageTk.PhotoImage(image)

label1 = Label(image=img, bg='#333538')
label1.image = img
label1.place(relx = -0.003, rely = 0.5, anchor='w')

# Load the game logo
image2 = Image.open("logo.png")
img2 = ImageTk.PhotoImage(image2)

label1 = Label(image=img2, bg='#333538')
label1.image2 = img2
label1.place(relx = 0.75, rely = 0.23, anchor='center')

# Random Splash Text
splashno = random.randrange(1, 4)

splashs = Label(text=splash[splashno], bg='#333538', fg='#ffffff')
splashs.place(relx = 0.75, rely = 0.36, anchor='center')

# Define the username entry field
user = customtkinter.CTkEntry(master=root, placeholder_text="Username", width=200)
user.place(relx = 0.75, rely = 0.5, anchor = 'center')

# Define the password entry field
password = customtkinter.CTkEntry(master=root, placeholder_text="Password", width=200)
password.place(relx = 0.75, rely = 0.6, anchor = 'center')

def checkbox_event():
    print("checkbox toggled, current value: bruh")

checkbox = customtkinter.CTkCheckBox(master=root, text="Remember username?", command=checkbox_event, onvalue="on", offvalue="off")
checkbox.place(relx = 0.722, rely = 0.67, anchor = 'center')

# Define the login button
button = customtkinter.CTkButton(master=root, text="Login")
button.place(relx = 0.75, rely = 0.75, anchor = 'center')

root.mainloop()