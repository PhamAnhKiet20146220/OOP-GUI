import tkinter as tk

def button_state():
    if var.get() == 1:
        button.config(state=tk.NORMAL)  # Bật nút
    elif var.get() == 2:
        button.config(state=tk.DISABLED)  # Vô hiệu hóa nút

def nut1():
    label1.config(text="hello")

root = tk.Tk()
root.title("Ví dụ Radiobutton")

var = tk.IntVar()

radio1 = tk.Radiobutton(root, text="Radio 1", variable=var, value=1, command=button_state) 
radio1.pack()

radio2 = tk.Radiobutton(root, text="Radio 2", variable=var, value=2, command=button_state)
radio2.pack()

label1=tk.Label(root, text="")
label1.pack()

button = tk.Button(root, text="Nút", state=tk.DISABLED, command=nut1)
button.pack()

root.mainloop()