import customtkinter as ctk

def close_menu() -> None:
    exit(-1)

class TitleBar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=0)

        self.title_label = ctk.CTkLabel(master=self, text="PokeMMO Menu", font=("Tahoma", 16))
        self.title_label.pack(anchor="n", side="left", padx=(150, 0))

        self.close_button = ctk.CTkButton(master=self, text="X", font=("Tahoma", 16), corner_radius=0, width=50, command=close_menu)
        self.close_button.pack(anchor="ne", side="right")

        self.pack(fill="x", anchor="n")

        def get_pos(event):
            xwin = master.winfo_x()
            ywin = master.winfo_y()
            startx = event.x_root
            starty = event.y_root

            ywin = ywin - starty
            xwin = xwin - startx

            def move_window(event):
                master.geometry("400x280" + '+{0}+{1}'.format(event.x_root + xwin, event.y_root + ywin))
                startx = event.x_root
                starty = event.y_root

            self.bind('<B1-Motion>', move_window)
            self.title_label.bind('<B1-Motion>', move_window)

        self.bind('<Button-1>', get_pos)
        self.title_label.bind('<Button-1>', get_pos)
