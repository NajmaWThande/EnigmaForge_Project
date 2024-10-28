from tkinter import *
from tkinter import messagebox
import base64
from PIL import Image, ImageTk

def decrypt():
    password = code.get()

    if password == "1234":
        screen2 = Toplevel(screen) 
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#7E57C2")

        message = text1.get(1.0, END).strip()
        try:
            decode_message = message.encode("ascii")
            base64_bytes = base64.b64decode(decode_message)
            decrypted_message = base64_bytes.decode("ascii")

            Label(screen2, text="DECRYPTED", font="arial 12", 
                  fg="white", bg="#7E57C2").grid(row=0, column=0, pady=10)
            text2 = Text(screen2, font="Roboto 10", 
                         bg="white", relief=GROOVE, wrap=WORD, bd=0)
            text2.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

            screen2.grid_rowconfigure(1, weight=1)
            screen2.grid_columnconfigure(0, weight=1)

            text2.insert(END, decrypted_message)
        except Exception as e:
            messagebox.showerror("Decryption Error",
                                  f"An error occurred: {str(e)}")

    elif password == "":
        messagebox.showerror("Decryption", "Input Password")

    else:
        messagebox.showerror("Decryption", "Invalid Password")

def encrypt():
    password = code.get()

    if password == "1234":
        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#7E57C2")

        message = text1.get(1.0, END).strip()
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypted_message = base64_bytes.decode("ascii")

        Label(screen1, text="ENCRYPTED", font="arial 12",
               fg="white", bg="#7E57C2").grid(row=0, column=0, pady=10)
        text2 = Text(screen1, font="Roboto 10", bg="white", 
                     relief=GROOVE, wrap=WORD, bd=0)
        text2.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        screen1.grid_rowconfigure(1, weight=1)
        screen1.grid_columnconfigure(0, weight=1)

        text2.insert(END, encrypted_message)

    elif password == "":
        messagebox.showerror("Encryption", "Input Password")

    else:
        messagebox.showerror("Encryption", "Invalid Password")

def main_screen():
    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("400x400")
    screen.configure(bg="#212121")

    # icon
    image_icon = Image.open("/home/najmathande/Desktop/IST_DIPLOMA/Cybersecurity/Project/EnigmaForge/key.png")
    image_icon_resized = image_icon.resize((50, 50))
    image_icon_tk = ImageTk.PhotoImage(image_icon_resized)
    screen.iconphoto(False, image_icon_tk)
    screen.title("EnigmaForge")

    def reset():
        code.set("")
        text1.delete(1.0, END)

    Label(screen, text="Enter text for encryption and decryption", fg="white", bg="#212121", 
          font=("Calibri", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
    text1 = Text(screen, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    Label(screen, text="Enter secret key for encryption and decryption", fg="white", bg="#212121", 
          font=("Calibri", 12)).grid(row=2, column=0, padx=10, pady=10, sticky="w")

    code = StringVar()
    Entry(screen, textvariable=code, width=20, bd=0, font=("arial", 24), show="*").grid(row=3,
     column=0, padx=10, pady=10, sticky="w")

    Button(screen, text="ENCRYPT", height="2", width=20, bg="#7E57C2", 
           fg="white", bd=0, command=encrypt).grid(row=4, column=0, padx=10, pady=5, sticky="w")
    Button(screen, text="DECRYPT", height="2", width=20, bg="#9575CD",
            fg="white", bd=0, command=decrypt).grid(row=4, column=0, padx=10, pady=5, sticky="e")
    Button(screen, text="RESET", height="2", width=2, bg="#B39DDB", 
           fg="white", bd=0, command=reset).grid(row=5, column=0, padx=15, pady=10, sticky="we")

    background_label = Label(screen, image=image_icon_tk, bg="#212121")
    background_label.place(relx=1, rely=1, anchor=SE)

    screen.grid_rowconfigure(1, weight=1)
    screen.grid_columnconfigure(0, weight=1)

    screen.mainloop()

main_screen()
