import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from steganography_tool import hide_text_in_image, extract_text_from_image

def select_image():
    filename = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if filename:
        img = Image.open(filename)
        img.thumbnail((300, 300))
        img = ImageTk.PhotoImage(img)
        image_label.config(image=img)
        image_label.image = img
        image_path.set(filename)

def embed_text():
    if not image_path.get() or not text_entry.get() or not key_entry.get():
        messagebox.showerror("Error", "All fields are required!")
        return
    output_file = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if output_file:
        hide_text_in_image(image_path.get(), text_entry.get(), output_file, key_entry.get().encode())
        messagebox.showinfo("Success", "Text hidden in image successfully!")

def extract_text():
    if not image_path.get() or not key_entry.get():
        messagebox.showerror("Error", "All fields are required!")
        return
    extracted_text = extract_text_from_image(image_path.get(), key_entry.get().encode())
    messagebox.showinfo("Extracted Text", extracted_text)

app = tk.Tk()
app.title("Steganography Tool")

image_path = tk.StringVar()

tk.Button(app, text="Select Image", command=select_image).pack()
image_label = tk.Label(app)
image_label.pack()

tk.Label(app, text="Enter Text to Hide").pack()
text_entry = tk.Entry(app, width=40)
text_entry.pack()

tk.Label(app, text="Enter 16-byte AES Key").pack()
key_entry = tk.Entry(app, show="*", width=40)
key_entry.pack()

tk.Button(app, text="Embed Text", command=embed_text).pack()
tk.Button(app, text="Extract Text", command=extract_text).pack()

app.mainloop()
