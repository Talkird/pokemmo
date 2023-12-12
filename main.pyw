import customtkinter as ctk
from PIL import Image
from components.TabView import TabView
from components.TitleBar import TitleBar

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x280")
        self.resizable(False, False)
        self.title("PokeMMO Menu")
        self.overrideredirect(True)
        self.attributes('-topmost', True)
        self.attributes('-alpha', 0.95)

        # widgets
        self.title_bar = TitleBar(master=self, title="PokeMMO Menu")
        self.tab_view = TabView(master=self)
        self.tab_view.pack(fill="both", expand=True, padx=15, pady=(0,15))

ctk.set_default_color_theme("green")
app = App()
app.mainloop()