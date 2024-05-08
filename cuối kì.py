#thêm các thư viện cần thiết
from tkinter import *

root = Tk()
root.title("cua so 1")

 #lấy vị trí màn hình
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Tính toán vị trí giữa màn hình và hiện cửa sổ 1 ở chính giữa
x = int((screen_width - 500) / 2)
y = int((screen_height - 500) / 2)
root.geometry(f"500x300+{x}+{y}")


mainloop()