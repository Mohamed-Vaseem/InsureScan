import customtkinter as ctk
from PIL import Image, ImageOps

from ui.styles import *

DISPLAY_SIZE = (500, 280)


class ImageCard(ctk.CTkFrame):

    def __init__(self, master, title):
        super().__init__(master, corner_radius=12)

        self.title = title
        self.photo = None

        self.build()

    def build(self):

        self.title_label = ctk.CTkLabel(
            self,
            text=self.title,
            font=HEADER_FONT
        )
        self.title_label.pack(pady=(15, 10))

        self.create_image_label()

    def create_image_label(self):

        self.image_label = ctk.CTkLabel(
            self,
            text="No Image",
            width=DISPLAY_SIZE[0],
            height=DISPLAY_SIZE[1],
            fg_color="#2B2B2B",
            corner_radius=8
        )

        self.image_label.pack(
            padx=20,
            pady=(0, 20),
            expand=True
        )

    def set_image(self, image):

        image = ImageOps.fit(
            image,
            DISPLAY_SIZE,
            method=Image.Resampling.LANCZOS
        )

        self.photo = ctk.CTkImage(
            light_image=image,
            dark_image=image,
            size=DISPLAY_SIZE
        )

        self.image_label.configure(
            image=self.photo,
            text=""
        )

    def clear(self):

        self.photo = None

        self.image_label.destroy()

        self.create_image_label()