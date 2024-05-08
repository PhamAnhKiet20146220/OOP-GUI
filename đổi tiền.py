#bài tập giao diện
from tkinter import *
root = Tk()

root.title("MONEY EXCHANGE")
root.geometry("700x500")

def callback():
    global a
    a = color.get()
    if a==0:    
        label1.configure(text = 'MỜI BẠN CHỌN LOẠI NGOẠI LỆ')
    if a==1:
        try:
            tien = int(E1.get())
            tien=tien*22000
            label1.configure(text = 'GIÁ TRỊ QUY ĐỔI: {} vnd'.format(tien))
            E1.delete(0,END)
        except:
             label1.configure(text = 'NHẬP SỐ LƯỢNG TIỀN CẦN ĐỔI')
             E1.delete(0,END)
    if a==2:
        try:
            tien = int(E1.get())
            tien=tien*26000
            label1.configure(text = 'GIÁ TRỊ QUY ĐỔI: {} vnd'.format(tien))
            E1.delete(0,END)
        except:
             label1.configure(text = 'NHẬP SỐ LƯỢNG TIỀN CẦN ĐỔI')
             E1.delete(0,END)
    if a==3:
        try:
            tien = int(E1.get())
            tien=tien*200
            label1.configure(text = 'GIÁ TRỊ QUY ĐỔI: {} vnd'.format(tien))
            E1.delete(0,END)
        except:
             label1.configure(text = 'NHẬP SỐ LƯỢNG TIỀN CẦN ĐỔI')
             E1.delete(0,END)

    
    
color = IntVar()
redbutton = Radiobutton(text='USD: 22000',font=("Arial", 22), var=color, value=1)
redbutton.place(x=50,y=100)
greenbutton = Radiobutton(text='EUR: 26000',font=("Arial", 22), var=color, value=2)
greenbutton.place(x=50,y=150)
bluebutton = Radiobutton(text='JYP:200',font=("Arial", 22), var=color, value=3)
bluebutton.place(x=50,y=200)

a = 0


E1=Entry(font=("Arial", 25),width=10)
E1.place(x=300,y=100)

B1 = Button(text="EXCHANGE",font=("Arial", 22),command=callback)
B1.place(x=300,y=150)

label1 = Label(root, text= "GIÁ TRỊ QUY ĐỔI:   vnd",font=("Arial", 22),fg='blue')
label1.place(x=130,y=350)


mainloop()
