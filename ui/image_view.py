import customtkinter as ctk

from ui.widgets.image_card import ImageCard
from ui.widgets.result_card import ResultCard


class ImageView(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.build()

    def build(self):

        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_rowconfigure(2, weight=0)

        self.original_card = ImageCard(
            self,
            "Original Image"
        )

        self.crop_card = ImageCard(
            self,
            "Vehicle Crop"
        )

        self.processed_card = ImageCard(
            self,
            "Preprocessed Image"
        )

        self.segmented_card = ImageCard(
            self,
            "Damage Detection"
        )

        self.results_card = ResultCard(self)

        self.original_card.grid(
            row=0,
            column=0,
            padx=15,
            pady=15,
            sticky="nsew"
        )

        self.crop_card.grid(
            row=0,
            column=1,
            padx=15,
            pady=15,
            sticky="nsew"
        )

        self.processed_card.grid(
            row=1,
            column=0,
            padx=15,
            pady=15,
            sticky="nsew"
        )

        self.segmented_card.grid(
            row=1,
            column=1,
            padx=15,
            pady=15,
            sticky="nsew"
        )

        self.results_card.grid(
            row=2,
            column=0,
            columnspan=2,
            padx=15,
            pady=(0, 15),
            sticky="ew"
        )