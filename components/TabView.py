import customtkinter as ctk
from PIL import Image

class TabView(ctk.CTkTabview):
    def __init__(self, master):
        super().__init__(master, corner_radius=12)

        #create tabs
        self.add("Payday")
        self.add("XP Grinder")
        self.add("Routes")
        self.add("Config")

        self.payday_switch = ctk.CTkSwitch(master=self.tab("Payday"),
                                           text="Enable payday",
                                           font=("Tahoma", 16)
                                           ).pack(padx=10, pady=15, anchor="w")

        self.payday_mode = ctk.CTkComboBox(master=self.tab("Payday"), 
                                           values=["Dragonspiral Tower", "Artisan Cave", "Undella Bay"],
                                           font=("Tahoma", 16)
                                           ).pack(fill="x", padx=10, pady=15)


        self.autoheal_enabled = ctk.CTkCheckBox(master=self.tab("Payday"),
                                                 text="Auto Heal",
                                                 font=("Tahoma", 16)
                                                 ).pack(side="left", padx=10, pady=15)

        self.discord_mode = ctk.CTkCheckBox(master=self.tab("Payday"),
                                                 text="Discord Mode",
                                                 font=("Tahoma", 16)
                                                 ).pack(side="right", padx=10, pady=15)

        self._segmented_button.configure(font=("Tahoma", 16))

