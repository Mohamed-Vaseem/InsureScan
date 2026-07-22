import customtkinter as ctk

from ui.styles import *


class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("InsureScan")

        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        self.resizable(False, False)

        self.build_ui()

    def build_ui(self):

        title = ctk.CTkLabel(
            self,
            text="InsureScan",
            font=TITLE_FONT
        )

        title.pack(pady=20)

        subtitle = ctk.CTkLabel(
            self,
            text="AI Powered Hyundai Damage Detection",
            font=HEADER_FONT
        )

        subtitle.pack()