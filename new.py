import customtkinter
from PIL import Image
import tkinter as tk
import os
from running import mainmenu1
from musicinput import musicinput
customtkinter.set_appearance_mode("dark")


class App(customtkinter.CTk):
    width = 900
    height = 600

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Welcome")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)
        
        def display_home():
            home = tk.Toplevel()
            home.title("Home Page")
            # add widgets to the home page
            label = tk.Label(home, text="Welcome to the Home Page!")
            label.pack()

        # load and create background image
        self.bg_image = customtkinter.CTkImage(Image.open("vector7.png"),
                                               size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=1, column=1)

        # create login frame
        self.login_frame = customtkinter.CTkFrame(self, corner_radius=3,width=500,height=400)
        self.login_frame.grid(row=1, column=1)
        self.login_label = customtkinter.CTkLabel(self.login_frame, text="WELCOME TO\nSIGN-I-FY",
                                                  font=customtkinter.CTkFont(family="DM sans", size=20, weight="bold"))
        self.login_label.grid(row=0, column=0, padx=30, pady=(70, 15))
      
        self.login_button = customtkinter.CTkButton(self.login_frame, text="Get started", width=200, fg_color="green",hover_color="#114a1b", command=mainmenu1)
        self.login_button.grid(row=3, column=0, padx=30, pady=(25, 35))
        
        self.login_button = customtkinter.CTkButton(self.login_frame, text="Set your Fav Music", width=200, command=musicinput,fg_color="#1b3285",hover_color="#1c2a5c")
        self.login_button.grid(row=3, column=0, padx=30, pady=(85, 15))
        
        

        # create main frame
      #self.main_frame = customtkinter.CTkFrame(self, corner_radius=0)
      # self.main_frame.grid_columnconfigure(0, weight=1)
      # self.main_label = customtkinter.CTkLabel(self.main_frame, text="CustomTkinter\nMain Page",
      #                                          font=customtkinter.CTkFont(size=20, weight="bold"))
      # self.main_label.grid(row=0, column=0, padx=30, pady=(30, 15))
      # self.back_button = customtkinter.CTkButton(self.main_frame, text="Back", width=200)
      # self.back_button.grid(row=1, column=0, padx=30, pady=(15, 15))


if __name__ == "__main__":
    app = App()
    app.mainloop()