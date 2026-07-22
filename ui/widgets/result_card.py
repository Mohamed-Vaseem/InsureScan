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

        # Damage
        self.damage = ctk.CTkLabel(
            self,
            text="Damage : --",
            anchor="w"
        )

        self.damage.pack(
            fill="x",
            padx=20,
            pady=(0, 5)
        )

        # Confidence
        self.confidence = ctk.CTkLabel(
            self,
            text="Confidence : --",
            anchor="w"
        )

        self.confidence.pack(
            fill="x",
            padx=20,
            pady=5
        )

        # Severity
        self.severity = ctk.CTkLabel(
            self,
            text="Severity : --",
            anchor="w"
        )

        self.severity.pack(
            fill="x",
            padx=20,
            pady=5
        )

        # Processing Time
        self.time = ctk.CTkLabel(
            self,
            text="Processing Time : --",
            anchor="w"
        )

        self.time.pack(
            fill="x",
            padx=20,
            pady=5
        )

        # Status
        self.status = ctk.CTkLabel(
            self,
            text="Status : Waiting",
            anchor="w"
        )

        self.status.pack(
            fill="x",
            padx=20,
            pady=(5, 20)
        )

    def update_results(self, result):

        self.damage.configure(
            text=f"Damage : {result.damage_type or '--'}"
        )

        self.confidence.configure(
            text=f"Confidence : {result.confidence or '--'}"
        )

        self.severity.configure(
            text=f"Severity : {result.severity or '--'}"
        )

        if result.processing_time is not None:
            self.time.configure(
                text=f"Processing Time : {result.processing_time:.3f} sec"
            )
        else:
            self.time.configure(
                text="Processing Time : --"
            )

        self.status.configure(
            text=f"Status : {result.message or 'Waiting'}"
        )