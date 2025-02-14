import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry_var.get()))
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + text)

root = tk.Tk()
root.title("GUI Calculator")
root.geometry("350x500")
root.configure(bg="#2C3E50")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font="Arial 24 bold", justify="right", bd=10, relief=tk.RIDGE, bg="#ECF0F1")
entry.pack(fill="both", ipadx=8, ipady=15, pady=15)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in buttons:
    frame = tk.Frame(root, bg="#2C3E50")
    frame.pack(expand=True, fill="both")
    for char in row:
        button = tk.Button(frame, text=char, font="Arial 18 bold", height=2, width=5, bd=5, relief=tk.RAISED, bg="#34495E", fg="white")
        button.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        button.bind("<Button-1>", on_click)

root.mainloop()
