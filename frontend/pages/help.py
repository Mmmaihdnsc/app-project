import customtkinter as ctk

class HelpPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#121212")
        
        label = ctk.CTkLabel(self, text="Help & Support", font=ctk.CTkFont(size=32, weight="bold"), text_color="#FFFFFF")
        label.pack(pady=(50, 20))
        
        info = ctk.CTkLabel(self, text="404 Placeholder Page - Coming Soon", font=ctk.CTkFont(size=16), text_color="#777777")
        info.pack(pady=20)
        
        btn = ctk.CTkButton(self, text="← Back to Home", height=40, fg_color="#1A1A1A", hover_color="#2A2A2A", corner_radius=20, command=lambda: controller.show_frame("HomePage"))
        btn.pack(pady=20)
