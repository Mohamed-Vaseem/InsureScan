from unittest import result

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
        self.geometry("1450x850")
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
            text="AI-Powered Vehicle Damage Detection",
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
            self.upload_image,
            self.detect_damage,
            self.clear_all
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
        self.sidebar.upload_button.configure(
            state="disabled"
        )

        path = filedialog.askopenfilename(
            title="Select Vehicle Image",
            filetypes=[("Images", "*.jpg *.jpeg *.png")]
        )

        if not path:
            return

        self.image_path = path

        image = self.pipeline.image_manager.load(path)

        original = Image.fromarray(
            cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        )

        self.content.original_card.set_image(original)

        self.sidebar.detect_button.configure(
            state="normal"
        )

        self.sidebar.status.configure(
            text="🟡 Image Loaded"
        )
        self.sidebar.upload_button.configure(
            state="normal"
        )
        
    def detect_damage(self):
        self.sidebar.detect_button.configure(
            state="disabled"
        )

        if self.image_path is None:
            return

        self.sidebar.status.configure(
            text="🟡 Processing..."
        )

        self.update()

        result = self.pipeline.process(self.image_path)

        if result.cropped is not None:

            crop = Image.fromarray(
                cv2.cvtColor(result.cropped, cv2.COLOR_BGR2RGB)
            )

            self.content.crop_card.set_image(crop)

        if result.preprocessed is not None:

            processed = Image.fromarray(
                cv2.cvtColor(result.preprocessed, cv2.COLOR_BGR2RGB)
            )

            self.content.processed_card.set_image(processed)

        if result.segmented is not None:

            segmented = Image.fromarray(
                cv2.cvtColor(result.segmented, cv2.COLOR_BGR2RGB)
            )

            self.content.segmented_card.set_image(segmented)

        self.content.results_card.update_results(result)

        self.sidebar.status.configure(
            text="🟢 Pipeline Completed"
        )
        self.sidebar.detect_button.configure(
            state="normal"
        )
        
    def clear_all(self):

        self.image_path = None

        # Reset image cards
        cards = [
            self.content.original_card,
            self.content.crop_card,
            self.content.processed_card,
            self.content.segmented_card
        ]

        for card in cards:
            card.image_label.configure(
                image=None,
                text="No Image"
            )
            card.photo = None

        # Reset detection summary
        self.content.results_card.damage.configure(
            text="Damage Type      : --"
        )

        self.content.results_card.confidence.configure(
            text="Confidence       : --"
        )

        self.content.results_card.severity.configure(
            text="Severity         : --"
        )

        self.content.results_card.time.configure(
            text="Processing Time  : --"
        )

        self.content.results_card.status.configure(
            text="Status           : Waiting",
            text_color="white"
        )

        # Reset sidebar
        self.sidebar.detect_button.configure(
            state="disabled"
        )

        self.sidebar.status.configure(
            text="⚪ Ready"
        )