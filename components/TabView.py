import customtkinter as ctk

class TabView(ctk.CTkTabview):
    def __init__(self, master):
        super().__init__(master, corner_radius=10)

        #create tabs
        self.add("Payday")
        self.add("GTL")
        self.add("XP Grinder")
        self.add("Config")

        #Payday Tab
        self.payday_switch = ctk.CTkSwitch(master=self.tab("Payday"),
                                           text="Enable payday",
                                           font=("Roboto", 16)
                                           ).pack(anchor="w", padx=10, pady=5)

        self.payday_mode = ctk.CTkComboBox(master=self.tab("Payday"), 
                                           values=["Dragonspiral Tower", "Artisan Cave", "Undella Bay"],
                                           font=("Roboto", 16),
                                           width=200,
                                           ).pack(anchor="w", padx=10, pady=5)

        self.payday_keybind = ctk.CTkComboBox(master=self.tab("Payday"), 
                                           values=["Space", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9"],
                                           font=("Roboto", 16)
                                           ).pack(anchor="w", padx=10, pady=5)

        self.autoheal_enabled = ctk.CTkCheckBox(master=self.tab("Payday"),
                                                 text="Auto Heal",
                                                 font=("Roboto", 16)
                                                 ).pack(anchor="w", padx=10, pady=5)

        self.discord_mode = ctk.CTkCheckBox(master=self.tab("Payday"),
                                                 text="Discord Mode",
                                                 font=("Roboto", 16)
                                                 ).pack(anchor="w", padx=10, pady=5)

        self._segmented_button.configure(font=("Roboto", 16))