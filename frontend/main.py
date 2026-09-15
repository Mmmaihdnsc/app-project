import customtkinter as ctk
from pages.home import HomePage
from pages.settings import SettingsPage
from pages.help import HelpPage
from pages.not_found import NotFoundPage

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("SignSpeak")
        self.geometry("1000x650")
        self.configure(fg_color="#121212") # Match the dark background
        
        # Container for pages
        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.container.pack(fill="both", expand=True)
        
        self.pages = {}
        
        for F in (HomePage, SettingsPage, HelpPage, NotFoundPage):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.pages[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        self.show_frame("HomePage")
        
    def show_frame(self, page_name):
        frame = self.pages[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()
