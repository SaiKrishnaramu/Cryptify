import customtkinter as ctk
from tkinter import messagebox
import base64

def decrypt():
    password = code.get()

    if password == "1234":
        screen2 = ctk.CTkToplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")

        message = text1.get("1.0", "end")
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypt = base64_bytes.decode("ascii")

        ctk.CTkLabel(screen2, text="DECRYPT", font=("Arial", 14)).place(x=10, y=0)
        text2 = ctk.CTkTextbox(screen2, font=("Roboto", 10), wrap="word", width=380, height=150)
        text2.place(x=10, y=40)

        text2.insert("end", decrypt)

    elif password == "":
        messagebox.showwarning("Encryption", "Input Password")

    elif password != "1234":
        messagebox.showerror("Encryption", "Invalid Password")

def encrypt():
    password = code.get()

    if password == "1234":
        screen1 = ctk.CTkToplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")

        message = text1.get("1.0", "end")
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        ctk.CTkLabel(screen1, text="ENCRYPT", font=("Arial", 14)).place(x=10, y=0)
        text2 = ctk.CTkTextbox(screen1, font=("Roboto", 10), wrap="word", width=380, height=150)
        text2.place(x=10, y=40)

        text2.insert("end", encrypt)

    elif password == "":
        messagebox.showwarning("Encryption", "Input Password")

    elif password != "1234":
        messagebox.showerror("Encryption", "Invalid Password")

def main_screen():
    global screen
    global code
    global text1

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    screen = ctk.CTk()
    screen.geometry("375x398")
    screen.title("Cryptify")


    # Set the icon for the window
    screen.iconbitmap(r"C:\Users\saikr\AppData\Local\Programs\Python\Python311\icon1.ico")


    def reset():
        code.set("")
        text1.delete("1.0", "end")

    ctk.CTkLabel(screen, text="Enter text for Encryption and Decryption", font=("Calibri", 13)).place(x=10, y=10)
    text1 = ctk.CTkTextbox(screen, font=("Roboto", 20), wrap="word", width=355, height=100)
    text1.place(x=10, y=50)

    ctk.CTkLabel(screen, text="Enter secret key for encryption and decryption", font=("Calibri", 13)).place(x=10, y=170)

    code = ctk.StringVar()
    ctk.CTkEntry(screen, textvariable=code, width=190, font=("Arial", 25), show="*").place(x=10, y=200)

    ctk.CTkButton(screen, text="ENCRYPT", height=40, width=170, fg_color="#ed3833", command=encrypt).place(x=10, y=250)
    ctk.CTkButton(screen, text="DECRYPT", height=40, width=170, fg_color="#00bd56", command=decrypt).place(x=200, y=250)
    ctk.CTkButton(screen, text="RESET", height=40, width=350, fg_color="#1089ff", command=reset).place(x=10, y=300)

    screen.mainloop()

main_screen()
