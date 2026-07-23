import customtkinter as ctk
from PIL import Image, ImageOps

from ui.styles import *

DISPLAY_SIZE = (500, 280)


class ImageCard(ctk.CTkFrame):

    def __init__(self, master, title):

        super().__init__(
            master,
            corner_radius=12
        )

        self.photo = None

        self.build(title)

    def build(self, title):

        title_label = ctk.CTkLabel(
            self,
            text=title,
            font=HEADER_FONT
        )

        title_label.pack(
            pady=(15, 10)
        )

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
            size=image.size
        )

        self.image_label.configure(
            image=self.photo,
            text=""
        )