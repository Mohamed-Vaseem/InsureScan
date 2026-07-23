import customtkinter as ctk

from ui.styles import *

class Sidebar(ctk.CTkFrame):

    def __init__(self, master, upload_callback, detect_callback, clear_callback):

        super().__init__(
            master,
            width=250,
            corner_radius=12
        )

        self.build(upload_callback, detect_callback, clear_callback)

    def build(self, upload_callback, detect_callback, clear_callback):

        self.pack_propagate(False)

        title = ctk.CTkLabel(
            self,
            text="Controls",
            font=HEADER_FONT
        )

        title.pack(pady=(20,30))

        self.upload_button = ctk.CTkButton(
            self,
            text="📂 Upload Image",
            command=upload_callback
        )

        self.upload_button.pack(
            padx=20,
            fill="x"
        )

        self.detect_button = ctk.CTkButton(
            self,
            text="🔍 Detect Damage",
            command=detect_callback,
            state="disabled"
        )

        self.detect_button.pack(
            padx=20,
            pady=20,
            fill="x"
        )
        
        self.clear_button = ctk.CTkButton(
            self,
            text="🗑 Clear",
            command=clear_callback
        )

        self.clear_button.pack(
            padx=20,
            pady=(0, 20),
            fill="x"
        )

        self.status = ctk.CTkLabel(
            self,
            text="🟢 Ready"
        )

        self.status.pack(
            side="bottom",
            pady=20
        )