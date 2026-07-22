import customtkinter as ctk
import cv2

from PIL import Image
from tkinter import filedialog

from ui.styles import *
from ui.sidebar import Sidebar
from ui.image_view import ImageView

from core.pipeline import ProcessingPipeline


class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("InsureScan")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.resizable(False, False)

        # Processing Pipeline
        self.pipeline = ProcessingPipeline()

        # Store selected image path
        self.image_path = None

        # Build UI
        self.create_layout()

    def create_layout(self):

        # -----------------------------
        # Header
        # -----------------------------
        title = ctk.CTkLabel(
            self,
            text="INSURESCAN",
            font=TITLE_FONT
        )

        title.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=(20, 5)
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
            pady=(0, 20)
        )

        # Window Layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # Sidebar
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

        # Main Content
        self.content = ImageView(self)

        self.content.grid(
            row=2,
            column=1,
            sticky="nsew",
            padx=(0, 20),
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

        self.image_path = path

        # Run the processing pipeline
        result = self.pipeline.process(path)

        # Convert original image (OpenCV BGR -> PIL RGB)
        original_image = Image.fromarray(
            cv2.cvtColor(result.original, cv2.COLOR_BGR2RGB)
        )

        processed_image = Image.fromarray(
            cv2.cvtColor(result.preprocessed, cv2.COLOR_BGR2RGB)
        )
        
        self.content.original_card.set_image(original_image)
        self.content.processed_card.set_image(processed_image)

        # Update result panel
        self.content.results_card.update_results(result)

        # Enable Detect button
        self.sidebar.detect_button.configure(
            state="normal"
        )

        # Update status
        self.sidebar.status.configure(
            text="🟢 Image Ready"
        )