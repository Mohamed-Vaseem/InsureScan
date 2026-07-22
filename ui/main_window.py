import customtkinter as ctk
import cv2

from ui.styles import *
from ui.sidebar import Sidebar
from ui.image_view import ImageView
from tkinter import Image, filedialog
from utils.image_utils import load_image
from preprocessing.preprocess import preprocess

class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("InsureScan")

        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        self.resizable(False, False)

        self.create_layout()
        self.image_path = None
        self.original_cv_image = None
        self.preprocessed_cv_image = None

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

    # Store path
        self.image_path = path

    # Read using OpenCV
        self.original_cv_image = cv2.imread(path)

    # Run preprocessing
        self.preprocessed_cv_image = preprocess(
            self.original_cv_image.copy()
        )

    # Display original image
        original_image = load_image(path)
        self.content.original_card.set_image(original_image)

    # Display processed image
        processed_rgb = cv2.cvtColor(
            self.preprocessed_cv_image,
            cv2.COLOR_BGR2RGB
        )

        from PIL import Image

        processed_pil = Image.fromarray(processed_rgb)

        self.content.processed_card.set_image(processed_pil)

    # Update UI
        self.sidebar.detect_button.configure(
            state="normal"
        )

        self.sidebar.status.configure(
            text="🟢 Image Ready"
        )