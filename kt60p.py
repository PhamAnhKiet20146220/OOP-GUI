from tkinter import *
c=0
def doi():
    global c
    a='VND'
    b='USD'
    c=c+1
    cdich.delete(0,END)
    dic.delete(0,END)
    if c%2!=0:
        cdich.insert(0,a) 
        dic.insert(0,b) 
    else: 
        cdich.insert(0,b) 
        dic.insert(0,a)
    if c==6:c=0 
def dich():
    global c
    try:
        st=int(sotien.get())
        a= cdich.get()
        d= dic.get()
        if a!='' and d!='':
            if a=='VND' and d=='USD':
                loi.configure(text=' {} VND='.format(st))
                ketqua.configure(text=' {} USD'.format(st/24000))
            elif a=='USD' and d=='VND':
                loi.configure(text=' {}  USD='.format(st))
                ketqua.configure(text=' {} VND'.format(st*24000))
            else:
                loi.configure(text=' Error ')
                ketqua.configure(text='  ')
        else:
            loi.configure(text=' Error ')
            ketqua.configure(text=' ')
    except:
        loi.configure(text=' Error ')
        ketqua.configure(text='  ')
root = Tk()
root.geometry("1000x450")
#tạo labelvà chổ nhập giá trị
lb1 = Label(text='From',font=('times',24))
lb2 = Label(text='To',font=('times',24))
cdich = Entry(font=('Verdana', 24, 'bold'),width=10)
dic  = Entry(font=('Verdana', 24, 'bold'),width=10)
ketqua= Label(text='',font=('times',24))
loi= Label(text='',font=('times',24))
lb3 = Label(text='Amount',font=('times',24))
sotien = Entry(font=('Verdana', 24, 'bold'),width=10)

lb3.place(x=10, y=50)
sotien.place(x=10, y=100)
loi.place(x=10, y=175)
ketqua.place(x=10, y=215)
lb1.place(x=375, y=50)
lb2.place(x=650, y=50)
cdich.place(x=300, y=100)
dic.place(x=600, y=100)

#dele
chuyen = Button(text='<->', font=('Verdana', 13),command=doi)
chuyen.place(x=525, y=52)
#ĐỔI
DOI = Button(text='Convert', font=('Verdana', 15),command=dich)
DOI.place(x=800, y=200)

cdich.insert(0,'USD') 
dic.insert(0,'VND') 

root.bind('<Return>',lambda dummy=0:dich())
mainloop()
