import tkinter as tk
import random

print("DLSS 6.9 running...\nClose window to stop frame counter")

def update_label():
    number = random.randint(1000, 1500)
    canvas.itemconfig(text_item, text=f"{number} FPS")
    root.after(16, update_label)

root = tk.Tk()
root.overrideredirect(True)
root.geometry("+0+0")
root.attributes("-topmost", True)
root.wm_attributes("-transparentcolor", "white")

canvas = tk.Canvas(root, width=400, height=200, bg="white", highlightthickness=0)
canvas.pack()

text_item = canvas.create_text(150, 50, text="0 FPS", font=("Helvetica", 48), fill="light green")

update_label()
root.mainloop()
