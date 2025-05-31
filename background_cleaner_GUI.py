from rembg import remove
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox
import os

def select_image():
    file_path = filedialog.askopenfilename(
        title="Select Image",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
    )
    
    if not file_path:
        return
    
    try:
        inp = Image.open(file_path)
        result = remove(inp)
        
        output_path = os.path.splitext(file_path)[0] + "_no_bg.png"
        result.save(output_path)
        
        messagebox.showinfo("Success", f"Background removed!\nSaved as:\n{output_path}")
        
        # Show result image
        result.thumbnail((300, 300))
        result_tk = ImageTk.PhotoImage(result)
        label_result.config(image=result_tk)
        label_result.image = result_tk

    except Exception as e:
        messagebox.showerror("Error", str(e))


# GUI Setup
root = tk.Tk()
root.title("Image Background Remover")
root.geometry("400x450")
root.config(bg="#f0f0f0")

tk.Label(root, text="Background Remover", font=("Helvetica", 16), bg="#f0f0f0").pack(pady=10)

tk.Button(root, text="Select Image", command=select_image, font=("Arial", 12), bg="#4CAF50", fg="white").pack(pady=20)

label_result = tk.Label(root)
label_result.pack(pady=10)

root.mainloop()
