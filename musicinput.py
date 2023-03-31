import os
import customtkinter
from tkinter import messagebox


# create the main window
def musicinput():
        window=customtkinter.CTkToplevel()
        window.geometry("700x580")
        window.title("SIGN-I-FY")

        # create a label to prompt the user for input
        label = customtkinter.CTkLabel(window, text="Enter the Link of your favourite music:")
        label.pack(pady=22)

        # create an entry field for the user to enter text
        entry =  customtkinter.CTkEntry(window,width=220)
        entry.pack()
        def show_alert():
            messagebox.showinfo("File Saved", "Your favourite music has been set")

        # create a button to write the text to a file
        def write_to_file():
            text = entry.get()
            if text !='':
                with open('link.txt', 'r+') as file:
                    check_file = os.stat("link.txt").st_size
                    if check_file == 0:
                        file.write(text)
                    else:
                        file.seek(0)
                        file.truncate(0)
                        file.write(text)
                file.close()
                show_alert()
                window.destroy()
            else:
                messagebox.showinfo("Invalid","Enter the URL first")
                

        button = customtkinter.CTkButton(window, text="Submit", command=write_to_file)
        button.pack(pady=18)
        window.grab_set()
        return window

# start the event loop

