import customtkinter as ctk
from PIL import Image

app = ctk.CTk()

img = Image.new("RGB", (200, 100), "red")
photo = ctk.CTkImage(light_image=img, dark_image=img, size=(200, 100))

label = ctk.CTkLabel(app, image=photo, text="")
label.pack(padx=20, pady=20)

def clear():
    label.configure(image=None, text="No Image")

def show():
    label.configure(image=photo, text="")

ctk.CTkButton(app, text="Clear", command=clear).pack()
ctk.CTkButton(app, text="Show", command=show).pack()

app.mainloop()