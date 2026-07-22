import customtkinter as ctk

from ui.styles import *
from PIL import Image
import customtkinter as ctk

class ImageCard(ctk.CTkFrame):

    def __init__(self, master, title):

        super().__init__(
            master,
            corner_radius=12
        )

        self.build(title)
        self.photo = None

    def build(self, title):

        title_label = ctk.CTkLabel(
            self,
            text=title,
            font=HEADER_FONT
        )

        title_label.pack(pady=(15,10))

        self.image_label = ctk.CTkLabel(
            self,
            text="No Image",
            width=400,
            height=300,
            corner_radius=10
        )

        self.image_label.pack(
            padx=20,
            pady=20,
            expand=True
        )
    def set_image(self, image):

        self.photo = ctk.CTkImage(
            light_image=image,
            dark_image=image,
            size=image.size
        )

        self.image_label.configure(
            image=self.photo,
            text=""
        )