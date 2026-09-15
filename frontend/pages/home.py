import customtkinter as ctk
from utils.icon_loader import load_icon

class HomePage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#121212")
        self.controller = controller

        # --- Load Icons (from Icons8) ---
        self.icon_settings = load_icon("settings", color="777777", size=24)
        self.icon_help = load_icon("help", color="777777", size=24)
        self.icon_arrow = load_icon("external-link", color="777777", size=18)
        self.icon_camera = load_icon("camera", color="242424", size=80)
        self.icon_globe = load_icon("globe", color="777777", size=32)
        self.icon_record = load_icon("record", color="777777", size=32)

        # --- Top Bar Capsule ---
        self.top_bar_container = ctk.CTkFrame(self, fg_color="transparent")
        self.top_bar_container.pack(fill="x", padx=30, pady=(25, 10))

        self.top_bar = ctk.CTkFrame(self.top_bar_container, fg_color="#181818", corner_radius=25, border_width=1, border_color="#242424")
        self.top_bar.pack(fill="x", ipady=5) 

        # Logo Frame
        self.logo_frame = ctk.CTkFrame(self.top_bar, fg_color="transparent")
        self.logo_frame.pack(side="left", padx=30, pady=10)

        self.logo_sign = ctk.CTkLabel(self.logo_frame, text="SIGN", font=ctk.CTkFont(family="Arial", size=24, weight="bold"), text_color="#E6E6E6")
        self.logo_sign.pack(side="left")
        
        self.logo_speak = ctk.CTkLabel(self.logo_frame, text="SPEAK", font=ctk.CTkFont(family="Arial", size=24, weight="bold"), text_color="#959595")
        self.logo_speak.pack(side="left")

        # Top Right Buttons Frame
        self.top_right_frame = ctk.CTkFrame(self.top_bar, fg_color="transparent")
        self.top_right_frame.pack(side="right", padx=20)

        self.contact_btn = ctk.CTkButton(
            self.top_right_frame, 
            text="Contact ", 
            image=self.icon_arrow,
            compound="right",
            width=100, 
            height=36, 
            fg_color="#121212", 
            hover_color="#1E1E1E", 
            corner_radius=18, 
            border_width=1,
            border_color="#242424",
            font=ctk.CTkFont(weight="bold"), 
            text_color="#959595", 
            command=lambda: controller.show_frame("NotFoundPage")
        )
        self.contact_btn.pack(side="right", padx=(10, 0))

        self.help_btn = ctk.CTkButton(
            self.top_right_frame, 
            text="", 
            image=self.icon_help,
            width=36, 
            height=36, 
            fg_color="#121212", 
            hover_color="#1E1E1E", 
            corner_radius=18, 
            border_width=1,
            border_color="#242424",
            command=lambda: controller.show_frame("HelpPage")
        )
        self.help_btn.pack(side="right", padx=5)

        self.settings_btn = ctk.CTkButton(
            self.top_right_frame, 
            text="", 
            image=self.icon_settings,
            width=36, 
            height=36, 
            fg_color="#121212", 
            hover_color="#1E1E1E", 
            corner_radius=18, 
            border_width=1,
            border_color="#242424",
            command=lambda: controller.show_frame("SettingsPage")
        )
        self.settings_btn.pack(side="right", padx=5)

        # --- Main Content ---
        self.main_content = ctk.CTkFrame(self, fg_color="transparent")
        self.main_content.pack(fill="both", expand=True, padx=30, pady=15)
        
        self.main_content.grid_columnconfigure(0, weight=1)
        self.main_content.grid_columnconfigure(1, weight=2)
        self.main_content.grid_rowconfigure(0, weight=1)
        self.main_content.grid_rowconfigure(1, weight=2)

        # Left Panel (Camera)
        self.camera_panel = ctk.CTkFrame(self.main_content, fg_color="#181818", corner_radius=24, border_width=1, border_color="#242424")
        self.camera_panel.grid(row=0, column=0, rowspan=2, sticky="nsew", padx=(0, 15))
        
        self.camera_icon_label = ctk.CTkLabel(self.camera_panel, text="", image=self.icon_camera)
        self.camera_icon_label.place(relx=0.5, rely=0.45, anchor="center")
        
        self.camera_label = ctk.CTkLabel(self.camera_panel, text="Enable Camera To Use", font=ctk.CTkFont(family="Arial", size=16, weight="bold"), text_color="#5E5E5E")
        self.camera_label.place(relx=0.5, rely=0.55, anchor="center")

        # Right Top Panel (Letters/Words)
        self.letters_panel = ctk.CTkFrame(self.main_content, fg_color="#181818", corner_radius=24, border_width=1, border_color="#242424")
        self.letters_panel.grid(row=0, column=1, sticky="nsew", pady=(0, 15))
        
        self.letters_label = ctk.CTkLabel(self.letters_panel, text="Translated Letters / Words", font=ctk.CTkFont(family="Arial", size=16, weight="bold"), text_color="#5E5E5E")
        self.letters_label.place(relx=0.5, rely=0.5, anchor="center")

        # Right Bottom Panel (Sentence)
        self.sentence_panel = ctk.CTkFrame(self.main_content, fg_color="#181818", corner_radius=24, border_width=1, border_color="#242424")
        self.sentence_panel.grid(row=1, column=1, sticky="nsew")
        
        self.sentence_label = ctk.CTkLabel(self.sentence_panel, text="Translated Sentence", font=ctk.CTkFont(family="Arial", size=16, weight="bold"), text_color="#5E5E5E")
        self.sentence_label.place(relx=0.5, rely=0.5, anchor="center")

        # --- Bottom Bar ---
        self.bottom_bar = ctk.CTkFrame(self, fg_color="transparent")
        self.bottom_bar.pack(fill="x", padx=30, pady=(15, 30))

        # Start button (wide capsule)
        self.start_btn = ctk.CTkButton(
            self.bottom_bar, 
            text="START", 
            height=54, 
            fg_color="#181818", 
            hover_color="#242424", 
            corner_radius=27, 
            border_width=1, 
            border_color="#242424", 
            font=ctk.CTkFont(family="Arial", size=16, weight="bold"), 
            text_color="#5E5E5E", 
            command=self.toggle_start
        )
        self.start_btn.pack(side="left", fill="x", expand=True, padx=(0, 15))

        # Language button (Circle)
        self.lang_btn = ctk.CTkButton(
            self.bottom_bar, 
            text="", 
            image=self.icon_globe,
            width=54, 
            height=54, 
            fg_color="#181818", 
            hover_color="#242424", 
            corner_radius=27, 
            border_width=1, 
            border_color="#242424", 
            command=lambda: controller.show_frame("NotFoundPage")
        )
        self.lang_btn.pack(side="left", padx=5)

        # Record button (Circle)
        self.record_btn = ctk.CTkButton(
            self.bottom_bar, 
            text="", 
            image=self.icon_record,
            width=54, 
            height=54, 
            fg_color="#181818", 
            hover_color="#242424", 
            corner_radius=27, 
            border_width=1, 
            border_color="#242424", 
            command=lambda: controller.show_frame("NotFoundPage")
        )
        self.record_btn.pack(side="left", padx=5)

        self.is_running = False

    def toggle_start(self):
        self.is_running = not self.is_running
        if self.is_running:
            self.start_btn.configure(text="STOP", text_color="#FF5555", border_color="#552222")
            self.camera_label.configure(text="Camera Active...", text_color="#55FF55")
        else:
            self.start_btn.configure(text="START", text_color="#5E5E5E", border_color="#242424")
            self.camera_label.configure(text="Enable Camera To Use", text_color="#5E5E5E")
            self.letters_label.configure(text="Translated Letters / Words")
            self.sentence_label.configure(text="Translated Sentence")
            
    def update_camera_frame(self, frame_image):
        pass

    def update_translated_text(self, letters_words, sentence):
        self.letters_label.configure(text=letters_words)
        self.sentence_label.configure(text=sentence)
