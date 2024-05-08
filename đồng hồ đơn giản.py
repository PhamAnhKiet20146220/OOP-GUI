from tkinter import *
import time

root = Tk()
root.title("Đồng hồ")
root.geometry("200x200")


def update_clock():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    root.after(1000, update_clock)
    
label = Label(root, font=("time",20))
label.pack()

update_clock()
root.mainloop()    

