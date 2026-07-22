import customtkinter as ctk

from ui.styles import *
from ui.sidebar import Sidebar
from ui.image_view import ImageView
from tkinter import filedialog
from utils.image_utils import load_image

class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("InsureScan")

        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        self.resizable(False, False)

        self.create_layout()

    def create_layout(self):

        title = ctk.CTkLabel(
            self,
            text="INSURESCAN",
            font=TITLE_FONT
        )
    
        title.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=(20,5)
        )

        subtitle = ctk.CTkLabel(
            self,
            text="AI Powered Hyundai Damage Detection",
            font=SUBTITLE_FONT
        )

        subtitle.grid(
            row=1,
            column=0,
            columnspan=2,
            pady=(0,20)
        )

    # Right Panel

        self.content = ctk.CTkFrame(
            self,
            corner_radius=12
        )

        self.content.grid(
            row=2,
            column=1,
            sticky="nsew",
            padx=(0,20),
            pady=20
        )

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.sidebar = Sidebar(
            self,
            self.upload_image
        )

        self.sidebar.grid(
            row=2,
            column=0,
            sticky="ns",
            padx=20,
            pady=20
        )

        self.content = ImageView(self)

        self.content.grid(
            row=2,
            column=1,
            sticky="nsew",
            padx=(0,20),
            pady=20
        )
    
    def upload_image(self):

        path = filedialog.askopenfilename(

            title="Select Vehicle Image",

            filetypes=[
                ("Images", "*.jpg *.jpeg *.png")
            ]
        )

        if not path:
            return

        image = load_image(path)

        self.content.original_card.set_image(image)

        self.sidebar.detect_button.configure(
            state="normal"
        )

        self.sidebar.status.configure(
            text="🟢 Image Loaded"
        )