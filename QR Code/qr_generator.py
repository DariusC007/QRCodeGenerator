import qrcode
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def generate_qr():
    url = entry.get()
    if not url:
        messagebox.showwarning("Warning", "Enter a valid link!")
        return
    img = qrcode.make(url)
    img.save("qrcode.png")

    # Show image
    img_tk = ImageTk.PhotoImage(img)
    label_img.config(image=img_tk)
    label_img.image = img_tk

    messagebox.showinfo("Succes", "The QR code was generated succesfully!")

# Main window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x400")

# UI
tk.Label(root, text="Enter the link:").pack(pady=10)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

tk.Button(root, text="Generate QR", command=generate_qr).pack(pady=10)

label_img = tk.Label(root)
label_img.pack(pady=20)


root.mainloop()
