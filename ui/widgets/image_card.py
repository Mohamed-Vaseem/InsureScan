import customtkinter as ctk
from PIL import Image

from ui.styles import *

DISPLAY_SIZE = (520, 340)


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

        title_label.pack(pady=(15, 10))

        self.image_label = ctk.CTkLabel(
            self,
            text="No Image",
            width=DISPLAY_SIZE[0],
            height=DISPLAY_SIZE[1]
        )

        self.image_label.pack(
            padx=20,
            pady=20,
            expand=True
        )

    def set_image(self, image):

        image = image.copy()
        image.thumbnail(DISPLAY_SIZE)

        self.photo = ctk.CTkImage(
            light_image=image,
            dark_image=image,
            size=image.size
        )

        self.image_label.configure(
            image=self.photo,
            text=""
        )