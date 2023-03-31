import customtkinter
import tkinter
from testnew import sign_language
from assistant import sign_assistant
from commonword import common_words
from nwevideo import videodetectionnew
import webbrowser
from tkinter import PhotoImage
import os

customtkinter.set_appearance_mode("dark")

def mainmenu1():
    app =customtkinter.CTkToplevel()
    app.geometry("900x780")
    app.title("SIGN-I-FY")
    def openinginfo(url):
        webbrowser.open_new_tab(url)
    def openinginfo1():
        file_path = os.path.abspath("D:\HandSignDetection\Indexoffront\index.html")
        url1 = "file://{}".format(file_path)
        webbrowser.open_new_tab(url1)
        
    container1 = customtkinter.CTkFrame(app)
    container1.grid(row=0, column=0, padx=18, pady=18, sticky="nsew")

    container2 = customtkinter.CTkFrame(app)
    container2.grid(row=0, column=1, padx=18, pady=18, sticky="nsew")

    container3 = customtkinter.CTkFrame(app)
    container3.grid(row=1, column=0, padx=18, pady=18, sticky="nsew")

    container4 = customtkinter.CTkFrame(app)
    container4.grid(row=1, column=1, padx=18, pady=18, sticky="nsew")
    

    # add buttons and labels to the containers
    
    label1 = customtkinter.CTkLabel(container1, text="Letter and number detection",
                                                  font=customtkinter.CTkFont(family="Calibri", size=20,weight="bold"))
    label1.place(relx=0.5, rely=0.32, anchor=tkinter.CENTER)
   
    button1 = customtkinter.CTkButton(container1, text="Click here",command=sign_language)
    button1.pack(pady=(155,0))
    button11 = customtkinter.CTkButton(container1, text="Learn ASL",command=lambda: openinginfo1(),fg_color="#1b2c6b")
    button11.pack(pady=(15,0))
    container1.pack_propagate(False)
    
    
    label2 = customtkinter.CTkLabel(container2, text="Sign Assistant",
                                                  font=customtkinter.CTkFont(family="Calibri", size=20,weight="bold"))
    label2.place(relx=0.5, rely=0.32, anchor=tkinter.CENTER)  
    button2 = customtkinter.CTkButton(container2, text="Explore",command=sign_assistant)
    button2.pack(pady=(155,0))
    button22 = customtkinter.CTkButton(container2, text="Info",command=lambda: openinginfo("signasst.html"),fg_color="#1b2c6b")
    button22.pack(pady=(15,0))
    container2.pack_propagate(False)
    
    label3 = customtkinter.CTkLabel(container3, text="Common words",
                                                  font=customtkinter.CTkFont(family="Calibri", size=20,weight="bold"))
    label3.place(relx=0.5, rely=0.32, anchor=tkinter.CENTER)  
    button3 = customtkinter.CTkButton(container3, text="Click here",command=common_words)
    button3.pack(pady=(155,0))
    button33 = customtkinter.CTkButton(container3, text="Learn more",command=lambda: openinginfo("word.html"),fg_color="#1b2c6b")
    button33.pack(pady=(15,0))
    container3.pack_propagate(False)
    
    def show_instructions():
        # Create new Toplevel window for pop-up box
        popup = customtkinter.CTkToplevel()
        popup.title("Instructions")
        popup.resizable(False, False)
        popup.geometry("350x210")
        icon = PhotoImage(file="info.png")
        # Create Label widget for message
        message = customtkinter.CTkLabel(popup, text="\n1)The video size should not exceed 100MB\n""\n2)Video length should be less than 5 minutes\n""\n3)Make sure the signs are clearly captured",image=icon,compound='top')
        message.pack(pady=20)

        # Add "OK" button to close pop-up
        ok_button = customtkinter.CTkButton(popup, text="OK", command=popup.destroy)
        ok_button.pack(pady=10)

        # Prevent interaction with main window while pop-up is open
        popup.grab_set()
    
    label4 = customtkinter.CTkLabel(container4, text="Video sign detection",
                                                  font=customtkinter.CTkFont(family="Calibri", size=20,weight="bold"))
    label4.place(relx=0.5, rely=0.32, anchor=tkinter.CENTER)  
    button4 = customtkinter.CTkButton(container4, text="Upload Video",command=videodetectionnew)
    button4.pack(pady=(155,0))
    button44 = customtkinter.CTkButton(container4, text="Instructions",command=show_instructions,fg_color="#1b2c6b")
    button44.pack(pady=(15,0))
    container4.pack_propagate(False)
    
    
    app.columnconfigure(0, weight=1)
    app.columnconfigure(1, weight=1)
    app.rowconfigure(0, weight=1)
    app.rowconfigure(1, weight=1)
    app.grab_set()

    return app


