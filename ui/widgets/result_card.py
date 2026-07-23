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
            text="Detection Summary",
            font=HEADER_FONT
        )
        title.pack(pady=(15, 20))

        self.damage = ctk.CTkLabel(
            self,
            text="Damage Type      : --",
            font=("Segoe UI", 15),
            anchor="w"
        )
        self.damage.pack(fill="x", padx=30, pady=6)

        self.confidence = ctk.CTkLabel(
            self,
            text="Confidence       : --",
            font=("Segoe UI", 15),
            anchor="w"
        )
        self.confidence.pack(fill="x", padx=30, pady=6)

        self.severity = ctk.CTkLabel(
            self,
            text="Severity         : --",
            font=("Segoe UI", 15),
            anchor="w"
        )
        self.severity.pack(fill="x", padx=30, pady=6)

        self.time = ctk.CTkLabel(
            self,
            text="Processing Time  : --",
            font=("Segoe UI", 15),
            anchor="w"
        )
        self.time.pack(fill="x", padx=30, pady=6)

        self.status = ctk.CTkLabel(
            self,
            text="Status           : Waiting",
            font=("Segoe UI", 15, "bold"),
            text_color="#4CAF50",
            anchor="w"
        )
        self.status.pack(fill="x", padx=30, pady=(6, 20))

    def update_results(self, result):

        if (
            result.damage is not None and
            result.damage.success and
            result.damage.count > 0
        ):

            detection = result.damage.detections[0]

            self.damage.configure(
                text=f"Damage : {detection.class_name}"
            )

            self.confidence.configure(
                text=f"Confidence : {detection.confidence:.2%}"
            )

            self.severity.configure(
                text="Severity : --"
            )

        else:

            self.damage.configure(
                text="Damage : None"
            )

            self.confidence.configure(
                text="Confidence : --"
            )

            self.severity.configure(
                text="Severity : --"
            )

        self.time.configure(
            text=f"Processing Time : {result.processing_time:.3f} sec"
        )

        self.status.configure(
            text=f"Status : {result.message}"
        )
        if result.success:
            self.status.configure(
                text="Status           : ✔ Pipeline Completed",
                text_color="#4CAF50"
            )
        else:
            self.status.configure(
                text=f"Status           : ✖ {result.message}",
                text_color="#F44336"
            )