import customtkinter as ctk

from ui.styles import *

class ResultCard(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            corner_radius=12
        )

        self.build()

    def build(self):

        title = ctk.CTkLabel(
            self,
            text="Detection Results",
            font=HEADER_FONT
        )

        title.pack(pady=15)

        self.damage = ctk.CTkLabel(
            self,
            text="Damage : --"
        )

        self.damage.pack(anchor="w", padx=20)

        self.confidence = ctk.CTkLabel(
            self,
            text="Confidence : --"
        )

        self.confidence.pack(anchor="w", padx=20, pady=5)

        self.time = ctk.CTkLabel(
            self,
            text="Processing Time : --"
        )

        self.time.pack(anchor="w", padx=20, pady=(5,20))