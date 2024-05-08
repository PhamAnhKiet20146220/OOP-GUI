import tkinter as tk
import mysql.connector
import pandas as pd
from PIL import ImageTk, Image
# Thư viện để tạo ra một cửa sổ thông báo
from tkinter import END, messagebox
# thư viện để kiểm tra Mật Khẩu
import re
# Thư viện để Lưu thông tin tài khoản
from openpyxl import load_workbook
import tkinter as tk
from tkinter import ttk
import mysql.connector
import pandas as pd
# Thư viện để tạo ra một cửa sổ thông báo
from tkinter import END, messagebox
# thư viện để kiểm tra Mật Khẩu
import re
# Thư viện để Lưu thông tin tài khoản
from openpyxl import load_workbook


# Class của cửa sổ đăng nhập
## Sẽ thêm vào đăng nhập của quản lý hay nhân viên bán hàng ##
class LoginWindow:
    def __init__(self):
        self.window = tk.Tk()
        # đổi màu cửa sổ
        self.window.configure(bg="light blue")
         #lấy vị trí màn hình
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # Tính toán vị trí giữa màn hình và hiện cửa sổ 1 ở chính giữa
        x = int((screen_width - 500) / 2)
        y = int((screen_height - 500) / 2)
        self.window.geometry(f"500x300+{x}+{y}")
        self.window.title("Đăng ký và Đăng nhập")

        # Tạo frame con bên trái để hiển thị bảng dữ liệu phim và thanh cuộn
        left_frame = tk.Frame(self.window,width=10,height=200)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        # Giới hạn kích thước của left_frame
        left_frame.pack_propagate(False)
        self.image = ImageTk.PhotoImage(Image.open("hinh.png"))
        label = tk.Label(left_frame, image=self.image)   
        label.pack(fill=tk.BOTH, expand=True)

        # Tạo frame con bên phải để hiển thị thông tin phim và các tùy chọn khác
        right_frame = tk.Frame(self.window)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        right_frame.pack_propagate(False)
        #hiển thị mật khẩu
        self.show_password = tk.BooleanVar()
        self.show_password.set(False)

        self.user_type = tk.StringVar()
        self.user_type.set("manager")  # Giá trị mặc định là "Quản Lý"
        self.radio_manager = tk.Radiobutton(right_frame, text="Quản lý", value="manager", variable=self.user_type)
        self.radio_manager.pack()
        self.radio_employee = tk.Radiobutton(right_frame, text="Nhân viên", value="employee", variable=self.user_type)
        self.radio_employee.pack()

        self.label_username = tk.Label(right_frame, text="Tên đăng nhập:")
        self.label_username.pack()
        self.entry_username = tk.Entry(right_frame)
        self.entry_username.pack()

        self.label_password = tk.Label(right_frame, text="Mật khẩu:")
        self.label_password.pack()
        self.entry_password = tk.Entry(right_frame, show="*")
        self.entry_password.pack()

        self.label_error = tk.Label(right_frame, text="")
        self.label_error.pack()

        self.button_register = tk.Button(right_frame, text="Đăng ký",bg="blue",width=10, height=2, command=self.open_register_window)
        self.button_register.pack()

        self.button_login = tk.Button(right_frame, text="Đăng nhập",bg="yellow",width=10, height=2, command=self.login)
        self.button_login.pack()

        self.checkbutton_show_password = tk.Checkbutton(right_frame, text="Hiển thị mật khẩu",variable=self.show_password,command=self.toggle_password_visibility)
        self.checkbutton_show_password.pack()

    # Hàm xử lý khi nút đăng kí được nhấn
    def open_register_window(self):
        register_window = RegisterWindow(self.window)

    # Hàm xử lý trình đăng nhập
    def login(self):
        self.username = self.entry_username.get()
        password = self.entry_password.get()

        # Kiểm tra xem người dùng đã nhập đủ thông tin hay chưa
        if not self.username or not password:
            self.label_error.configure(text='ERROR: Vui lòng nhập đầy đủ thông tin!', fg="red")
            return

        # Kết nối tới cơ sở dữ liệu MySQL
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="dinhan24092002",
            database="finalproject"
        )

        # Tạo đối tượng cursor để thực hiện các truy vấn
        cursor = cnx.cursor()

        # Thực hiện truy vấn SELECT để kiểm tra tên đăng nhập và mật khẩu
        select_query = "SELECT * FROM users WHERE username = %s AND password = %s"
        values = (self.username, password)
        cursor.execute(select_query, values)

        # Lấy kết quả truy vấn
        result = cursor.fetchall()

        # Đóng cursor
        cursor.close()

        # Đóng kết nối
        cnx.close()

        # Kiểm tra kết quả truy vấn
        # Không đăng nhập được
        if len(result) == 0:
            self.label_error.configure(text='ERROR: Tên đăng nhập hoặc mật khẩu không đúng!', fg="red")
            self.entry_username.delete(0, END)
            self.entry_password.delete(0, END)
        else:
            # Đăng nhập thành công
            #self.window.destroy()  # Đóng cửa sổ hiện tại
            # Tiếp tục làm việc trên cửa sổ chính
            self.open_main_window()

    # Hàm để mở cửa sổ chính
    def open_main_window(self):
        main_window = MainWindow(self.window,self.username)

    # Hàm để khởi tạo cửa số GUI
    def run(self):
        self.window.mainloop()

    # Hàm hiện mật khẩu
    def toggle_password_visibility(self):
        if self.show_password.get():
            self.entry_password.config(show="")
        else:
            self.entry_password.config(show="*")

# Class của cửa sổ đăng kí
class RegisterWindow:
    def __init__(self, parent):
        self.register_window = tk.Toplevel(parent)
         #lấy vị trí màn hình
        screen_width = self.register_window.winfo_screenwidth()
        screen_height = self.register_window.winfo_screenheight()

        # Tính toán vị trí giữa màn hình và hiện cửa sổ 1 ở chính giữa
        x = int((screen_width - 500) / 2)
        y = int((screen_height - 500) / 2)
        self.register_window.geometry(f"300x200+{x}+{y}")
        self.register_window.title("Đăng ký tài khoản")

        # Hiển thị mật khẩu
        self.show_password = tk.BooleanVar()
        self.show_password.set(False)

        self.label_username = tk.Label(self.register_window, text="Tên đăng nhập:")
        self.label_username.pack()
        self.entry_username = tk.Entry(self.register_window)
        self.entry_username.pack()

        self.label_password = tk.Label(self.register_window, text="Mật khẩu:")
        self.label_password.pack()
        self.entry_password = tk.Entry(self.register_window, show="*")
        self.entry_password.pack()

        self.label_confirm_password = tk.Label(self.register_window, text="Nhập lại mật khẩu:")
        self.label_confirm_password.pack()
        self.entry_confirm_password = tk.Entry(self.register_window, show="*")
        self.entry_confirm_password.pack()

        self.label_error = tk.Label(self.register_window, text="")
        self.label_error.pack()

        self.button_register = tk.Button(self.register_window, text="Đăng ký", command=self.register)
        self.button_register.pack()

        self.checkbutton_show_password = tk.Checkbutton(self.register_window, text="Hiển thị mật khẩu",variable=self.show_password,command=self.toggle_password_visibility)
        self.checkbutton_show_password.pack()
    # Hàm hiện mật khẩu
    def toggle_password_visibility(self):
        if self.show_password.get():
            self.entry_password.config(show="")
            self.entry_confirm_password.config(show="")
        else:
            self.entry_password.config(show="*")
            self.entry_confirm_password.config(show="*")
    # hàm xử lý trình đăng kí 
    def register(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        confirm_password = self.entry_confirm_password.get()

        #kiểm tra xem người dùng nhập đủ thông tin chưa
        if not username or not password or not confirm_password:
            self.label_error.configure(text='ERROR: Vui lòng nhập đầy đủ thông tin!', fg="red")
            return

        # Kiểm tra nhập lại mật khẩu khớp không
        if password != confirm_password:
            self.label_error.configure(text='ERROR: Mật khẩu không khớp!', fg="red")
            self.entry_username.delete(0, END)
            self.entry_password.delete(0, END)
            self.entry_confirm_password.delete(0, END)
        else:
            #Kiểm tra mật khẩu hợp lệ
            if not self.validate_password(password):
                self.label_error.configure(text='ERROR: Mật khẩu không hợp lệ!', fg="red")
                self.entry_username.delete(0, END)
                self.entry_password.delete(0, END)
                self.entry_confirm_password.delete(0, END)
            # Kiểm tra tên đăng nhập tồn tại
            if self.check_username_exists(username):
                self.label_error.configure(text='ERROR: Tên đăng nhập đã tồn tại!', fg="red")
                self.entry_username.delete(0, END)
                self.entry_password.delete(0, END)
                self.entry_confirm_password.delete(0, END)
            else:
                # Xử lý logic đăng ký tài khoản ở đây
                self.save_to_mysql(username, password)
                messagebox.showinfo("Thông báo", "Đăng ký thành công!")

    # Hàm kiểm tra các yêu cầu về mật khẩu (độ dài tối thiểu, chữ hoa, chữ thường, chữ số, ký tự đặc biệt)
    def validate_password(self, password):
        # Sử dụng biểu thức chính quy (regular expression)
        if len(password) < 8:
            return False
        if not re.search(r"[a-z]", password):
            return False
        if not re.search(r"\d", password):
            return False
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return False
        return True
    
    #Hàm kiểm tra tên đăng nhập
    def check_username_exists(self, username):
        try:
            # Kết nối tới cơ sở dữ liệu MySQL
            cnx = mysql.connector.connect(
                host="localhost",
                user="root",
                password="dinhan24092002",
                database="finalproject"
            )

            # Tạo đối tượng cursor để thực hiện các truy vấn
            cursor = cnx.cursor()

            # Thực hiện truy vấn SELECT để kiểm tra tên đăng nhập
            select_query = "SELECT * FROM users WHERE username = %s"
            values = (username,)
            cursor.execute(select_query, values)

            # Lấy kết quả truy vấn
            result = cursor.fetchall()

            # Đóng kết nối và cursor
            cursor.close()
            cnx.close()

            # Kiểm tra xem tên đăng nhập đã tồn tại hay chưa
            if len(result) > 0:
                return True
            else:
                return False
        except mysql.connector.Error as error:
            print("Lỗi khi kết nối và truy vấn dữ liệu từ MySQL:", error)
            return False
    
    #Hàm lưu thông tin đăng nhập
    def save_to_mysql(self, username, password):
        try:
            # Kết nối tới cơ sở dữ liệu MySQL
            cnx = mysql.connector.connect(
                host="localhost",
                user="root",
                password="dinhan24092002",
                database="finalproject"
            )

            # Tạo đối tượng cursor để thực hiện các truy vấn
            cursor = cnx.cursor()

            # Thực hiện truy vấn INSERT để lưu tài khoản vào bảng users
            insert_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
            values = (username, password)
            cursor.execute(insert_query, values)

            # Lưu các thay đổi vào cơ sở dữ liệu
            cnx.commit()

            # Đóng kết nối và cursor
            cursor.close()
            cnx.close()

            return True
        except mysql.connector.Error as error:
            print("Lỗi khi kết nối và lưu dữ liệu vào MySQL:", error)
            return False

# Class của cửa sổ chính
class MainWindow:
    def __init__(self, parent, username):
        self.Main_window = tk.Toplevel(parent)
        self.username=username
        # Lấy vị trí màn hình
        screen_width = self.Main_window.winfo_screenwidth()
        screen_height = self.Main_window.winfo_screenheight()

        # Tính toán vị trí giữa màn hình và hiện cửa sổ 1 ở chính giữa
        x = int((screen_width - 900) / 2)
        y = int((screen_height - 800) / 2)
        self.Main_window.geometry(f"1000x500+{x}+{y}")
        self.Main_window.title("KHA Cinema") 
        self.Main_window.configure(bg="gray")
        # Tạo frame chứa nội dung thay đổi
        self.content_frame = tk.Frame(self.Main_window)
        self.content_frame.pack(side=tk.RIGHT, fill=tk.BOTH,expand=True)
        self.image = ImageTk.PhotoImage(Image.open("3-min-1.jpg"))
        label = tk.Label(self.content_frame, image=self.image)   
        label.pack(fill=tk.BOTH, expand=True)

        # Hiển thị thông tin tài khoản
        self.account_frame = tk.Frame(self.Main_window)
        self.account_frame.pack(side=tk.TOP, fill=tk.X)

        # Hiển thị tên người đăng nhập
        self.label_username = tk.Label(self.Main_window, text="Tên người đăng nhập: " + username)
        self.label_username.pack()

        label_role = tk.Label(self.account_frame, text="Chức vụ: Quản lý")
        label_role.pack(side=tk.RIGHT, padx=5, pady=5)   

        # Tạo khung bên trái
        self.side_frame = tk.Frame(self.Main_window)
        self.side_frame.pack(side=tk.LEFT, fill=tk.Y)
        self.side_frame.configure(bg="khaki")
        # Thêm các tùy chọn
        button_order = tk.Button(self.side_frame, text="Doanh thu",bg='green', command=self.open_order_frame)
        button_order.pack(fill=tk.X, padx=10, pady=10)

        button_add_film = tk.Button(self.side_frame, text="Thêm Phim",bg="orange", command=self.show_add_film_frame)
        button_add_film.pack(fill=tk.X, padx=10, pady=10)

        button_price = tk.Button(self.side_frame, text="Quản Lý Giá",bg="pink", command=self.show_price_window)
        button_price.pack(fill=tk.X, padx=10, pady=10)

        button_ticket = tk.Button(self.side_frame, text="Ticket",bg="blue", command=self.show_ticket_window)
        button_ticket.pack(fill=tk.X, padx=10, pady=10)

        button_account = tk.Button(self.side_frame, text="Xem tài khoản", command=self.show_account_window)
        button_account.pack(fill=tk.X, padx=10, pady=10)

        button_exit = tk.Button(self.side_frame, text="Thoát",bg="gray", command=self.Main_window.quit)
        button_exit.pack(fill=tk.X, padx=10, pady=10)

    def open_order_frame(self):
        # Hiển thị frame Đơn hàng
        self.clear_content_frame()
        order_frame = OrderFrame(self)
        order_frame.search_movies()

    def show_add_film_frame(self):
        # Xóa nội dung hiện tại của frame
        self.clear_content_frame()

        # Hiển thị giao diện Thêm Phim
        add_film_frame = AddFilmFrame(self)

    def show_price_window(self):
        # Xóa nội dung hiện tại của frame
        self.clear_content_frame()

        # Thêm nội dung mới vào frame
        price_film_frame=PriceFrame(self)
    
    def show_ticket_window(self):
        # Xóa nội dung hiện tại của frame
        self.clear_content_frame()

        # Thêm nội dung mới vào frame
        ticket_frame=TicketFrame(self)

    def show_account_window(self):
        # Xóa nội dung hiện tại của frame
        self.clear_content_frame()

        # Thêm nội dung mới vào frame
        # Thêm nội dung mới vào frame
        show_account_frame=AccountFrame(self,self.username)

    def clear_content_frame(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
class OrderFrame:
    def __init__(self, parent):
        self.parent = parent

        # Tạo frame chứa nội dung Đơn hàng
        self.order_frame = tk.Frame(self.parent.content_frame)
        self.order_frame.pack(fill=tk.BOTH, expand=True)

        # Tạo frame con bên trái để hiển thị bảng dữ liệu phim và thanh cuộn
        left_frame = tk.Frame(self.order_frame,width=400, height=800)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        # Giới hạn kích thước của left_frame
        left_frame.pack_propagate(False)    

        # Tạo ô tìm kiếm
        search_button = tk.Button(left_frame, text="Tìm kiếm",bg='khaki', command=self.search_movies)
        search_button.pack()

        self.search_entry = tk.Entry(left_frame)
        self.search_entry.pack()

        # Tạo thanh cuộn
        scrollbar = tk.Scrollbar(left_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Tạo thanh cuộn ngang
        xscrollbar = tk.Scrollbar(left_frame, orient=tk.HORIZONTAL)
        xscrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        # Tạo bảng dữ liệu phim
        self.movie_table = ttk.Treeview(left_frame, yscrollcommand=scrollbar.set)
        # Thêm các cột và dữ liệu vào bảng dữ liệu phim
        self.movie_table['columns'] = ('STT', 'ReleaseDate', 'MovieTitle', 'Price','Order_number','Revenue')

        self.movie_table.column('STT', width=4)
        self.movie_table.column('ReleaseDate', width=50)
        self.movie_table.column('MovieTitle', width=200)
        self.movie_table.column('Price', width=10)
        self.movie_table.column('Order_number', width=10)
        self.movie_table.column('Revenue', width=10)
        self.movie_table.heading('STT', text='STT')
        self.movie_table.heading('ReleaseDate', text='ReleaseDate')
        self.movie_table.heading('MovieTitle', text='MovieTitle')
        self.movie_table.heading('Price', text='Price')
        self.movie_table.heading('Order_number', text='Order_number')
        self.movie_table.heading('Revenue', text='Revenue')

        # Tìm index của cột "MovieTitle"
        column_index = self.movie_table['columns'].index('MovieTitle')
        # Tính toán vị trí cuộn ngang của thanh cuộn
        scroll_position = column_index / len(self.movie_table['columns'])

        # Di chuyển thanh cuộn ngang đến vị trí mong muốn
        self.movie_table.xview_moveto(scroll_position)

        # Kết nối thanh cuộn với bảng dữ liệu phim
        scrollbar.config(command=self.movie_table.yview)
        # Kết nối thanh cuộn ngang với bảng dữ liệu phim
        self.movie_table.configure(xscrollcommand=xscrollbar.set)
        xscrollbar.config(command=self.movie_table.xview)

        # Hiển thị bảng dữ liệu phim
        self.movie_table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Gọi hàm để hiển thị dữ liệu phim từ MySQL
        self.load_movies()

        # Tạo frame con bên phải để hiển thị thông tin phim và các tùy chọn khác
        right_frame = tk.Frame(self.order_frame)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        # Giới hạn kích thước của left_frame
        right_frame.pack_propagate(False) 
        # Thêm nội dung mới vào frame bên phải
        label = tk.Label(right_frame, text="Thông tin phim")
        label.pack()

        # Tạo các label để hiển thị thông tin phim
        self.label_stt = tk.Label(right_frame, text="STT:",anchor="w")
        self.label_stt.pack(anchor="w")
        self.label_release_date = tk.Label(right_frame, text="Ngày phát hành:",anchor="w")
        self.label_release_date.pack(anchor="w")
        self.label_movie_title = tk.Label(right_frame, text="Tên phim:",anchor="w")
        self.label_movie_title.pack(anchor="w")
        self.label_price = tk.Label(right_frame, text="Đơn giá:",anchor="w")
        self.label_price.pack(anchor="w")
        self.label_order_number = tk.Label(right_frame, text="Số lượng đặt:",anchor="w")
        self.label_order_number.pack(anchor="w")
        self.label_revenue = tk.Label(right_frame, text="Doanh thu:",anchor="w")
        self.label_revenue.pack(anchor="w")

    def load_movies(self):
        # Kết nối tới cơ sở dữ liệu MySQL
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="dinhan24092002",
            database="finalproject"
        )
        cursor = cnx.cursor()

        # Truy vấn dữ liệu từ bảng dulieuphim trong MySQL
        query = "SELECT * FROM dulieuphim"
        cursor.execute(query)

        # Lấy tất cả các dòng kết quả từ truy vấn
        rows = cursor.fetchall()

        # Hiển thị dữ liệu trên bảng dữ liệu phim
        for row in rows:
            self.movie_table.insert('', 'end', values=row)

        # Đóng kết nối và cursor
        cursor.close()
        cnx.close()
    def search_movies(self):
        # Xóa nội dung hiện tại của bảng dữ liệu phim
        self.movie_table.delete(*self.movie_table.get_children())
        # Lấy từ khóa tìm kiếm từ entry
        search_query = self.search_entry.get()
        # Kết nối tới cơ sở dữ liệu MySQL
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="dinhan24092002",
            database="finalproject"
        )
        cursor = cnx.cursor()
        # Truy vấn dữ liệu phim từ MySQL dựa trên từ khóa tìm kiếm
        query = "SELECT * FROM dulieuphim WHERE MovieTitle LIKE %s OR STT LIKE %s"
        cursor.execute(query, ('%' + search_query + '%', '%' + search_query + '%'))
        # Lấy tất cả các dòng kết quả từ truy vấn
        rows = cursor.fetchall()
        # Hiển thị dữ liệu trên bảng dữ liệu phim   
        for row in rows:
            self.movie_table.insert('', 'end', values=row)
        # Đóng kết nối và cursor
        cursor.close()
        cnx.close()
        # Gắn sự kiện chọn dòng trong bảng dữ liệu phim
        self.movie_table.bind("<<TreeviewSelect>>", self.update_movie_info)
    def update_movie_info(self, event):
        # Xóa nội dung hiện tại của phần frame "Thông tin phim"
        self.clear_movie_info()

        # Lấy thông tin phim từ dòng được chọn trong bảng dữ liệu phim
        selected_item = self.movie_table.focus()
        movie_info = self.movie_table.item(selected_item, 'values')

        # Hiển thị thông tin phim trong frame "Thông tin phim"
        self.label_stt.config(text="STT: " + str(movie_info[0]))
        self.label_release_date.config(text="Ngày phát hành: " + str(movie_info[1]))
        self.label_movie_title.config(text="Tên phim: " + str(movie_info[2]))
        self.label_price.config(text="Đơn giá: " + str(movie_info[3]))
        self.label_order_number.config(text="Số lượng đặt: " + str(movie_info[4]))
        self.label_revenue.config(text="Doanh thu: " + str(movie_info[5]))

        # Hiển thị hình

    def clear_movie_info(self):
        # Xóa nội dung của các label trong phần frame "Thông tin phim"
        self.label_stt.config(text="STT:")
        self.label_release_date.config(text="Ngày phát hành:")
        self.label_movie_title.config(text="Tên phim:")
        self.label_price.config(text="Đơn giá:")
        self.label_order_number.config(text="Số lượng đặt:")
        self.label_revenue.config(text="Doanh thu:")
class AddFilmFrame:
    def __init__(self, parent):
        self.parent = parent
        # Tạo frame chứa nội dung Thêm phim
        self.add_film_frame = tk.Frame(self.parent.content_frame,width=400, height=800)
        self.add_film_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        # Giới hạn kích thước của left_frame
        self.add_film_frame.pack_propagate(False)

        # Tạo ô tìm kiếm
        search_button = tk.Button(self.add_film_frame, text="Tìm kiếm",bg='khaki', command=self.search_movies)
        search_button.pack()

        self.search_entry = tk.Entry(self.add_film_frame)
        self.search_entry.pack()

        # Tạo thanh cuộn
        scrollbar = tk.Scrollbar(self.add_film_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Tạo thanh cuộn ngang
        xscrollbar = tk.Scrollbar(self.add_film_frame, orient=tk.HORIZONTAL)
        xscrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        # Tạo bảng dữ liệu phim
        self.movie_table = ttk.Treeview(self.add_film_frame, yscrollcommand=scrollbar.set)
        # Thêm các cột và dữ liệu vào bảng dữ liệu phim
        self.movie_table['columns'] = ('STT', 'ReleaseDate', 'MovieTitle', 'Price','Order_number','Revenue')

        self.movie_table.heading('STT', text='STT')
        self.movie_table.heading('ReleaseDate', text='ReleaseDate')
        self.movie_table.heading('MovieTitle', text='MovieTitle')
        self.movie_table.heading('Price', text='Price')
        self.movie_table.heading('Order_number', text='Order_number')
        self.movie_table.heading('Revenue', text='Revenue')

        # Tìm index của cột "MovieTitle"
        column_index = self.movie_table['columns'].index('MovieTitle')
        # Tính toán vị trí cuộn ngang của thanh cuộn
        scroll_position = column_index / len(self.movie_table['columns'])

        # Di chuyển thanh cuộn ngang đến vị trí mong muốn
        self.movie_table.xview_moveto(scroll_position)

        # Kết nối thanh cuộn với bảng dữ liệu phim
        scrollbar.config(command=self.movie_table.yview)
        # Kết nối thanh cuộn ngang với bảng dữ liệu phim
        self.movie_table.configure(xscrollcommand=xscrollbar.set)
        xscrollbar.config(command=self.movie_table.xview)

        # Hiển thị bảng dữ liệu phim
        self.movie_table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Gọi hàm để hiển thị dữ liệu phim từ MySQL
        self.load_movies()

        # Tạo frame chứa nội dung Xóa phim
        self.delete_film_frame = tk.Frame(self.parent.content_frame)
        self.delete_film_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Tạo các phần nhập liệu cho các trường thông tin phim
        self.labels = ["ReleaseDate:", "Movie Title:", "Price:", "Order Number:", "Revenue:",
                       "Production Budget:", "Worldwide Gross:", "Domestic Gross:"]
        self.entries = []

        # Bố trí các label và entry trong frame Thêm phim
        for i, label_text in enumerate(self.labels):
            label = tk.Label(self.delete_film_frame, text=label_text, anchor="w")
            label.grid(row=i, column=0, padx=10, pady=5, sticky="w")

            entry = tk.Entry(self.delete_film_frame)
            entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")

            self.entries.append(entry)

        # Thêm nút Lưu để lưu thông tin phim
        button_save = tk.Button(self.delete_film_frame, text="Lưu",bg='Light green', command=self.save_film)
        button_save.grid(row=len(self.labels), columnspan=2, padx=10, pady=5)

        # Thêm label để hiển thị thông báo
        self.label_message = tk.Label(self.delete_film_frame, text="", fg="red")
        self.label_message.grid(row=len(self.labels) + 4, columnspan=2, padx=10, pady=5)

        # Tạo phần nhập liệu cho tên hoặc số thứ tự phim cần xóa trong frame Xóa phim
        label_delete = tk.Label(self.delete_film_frame, text="Nhập tên hoặc số thứ tự phim cần xóa:")
        label_delete.grid(row=len(self.labels) + 1, columnspan=2, padx=10, pady=5)

        self.entry_delete = tk.Entry(self.delete_film_frame)
        self.entry_delete.grid(row=len(self.labels) + 2, columnspan=2, padx=10, pady=5)

        button_delete = tk.Button(self.delete_film_frame, text="Xóa",bg='salmon', command=self.delete_film)
        button_delete.grid(row=len(self.labels) + 3, columnspan=2, padx=10, pady=5)

    def load_movies(self):
        # Kết nối tới cơ sở dữ liệu MySQL
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="dinhan24092002",
            database="finalproject"
        )
        cursor = cnx.cursor()

        # Truy vấn dữ liệu từ bảng dulieuphim trong MySQL
        query = "SELECT * FROM dulieuphim"
        cursor.execute(query)

        # Lấy tất cả các dòng kết quả từ truy vấn
        rows = cursor.fetchall()

        # Hiển thị dữ liệu trên bảng dữ liệu phim
        for row in rows:
            self.movie_table.insert('', 'end', values=row)

        # Đóng kết nối và cursor
        cursor.close()
        cnx.close()
    def search_movies(self):
        # Xóa nội dung hiện tại của bảng dữ liệu phim
        self.movie_table.delete(*self.movie_table.get_children())
        # Lấy từ khóa tìm kiếm từ entry
        search_query = self.search_entry.get()
        # Kết nối tới cơ sở dữ liệu MySQL
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="dinhan24092002",
            database="finalproject"
        )
        cursor = cnx.cursor()
        # Truy vấn dữ liệu phim từ MySQL dựa trên từ khóa tìm kiếm
        query = "SELECT * FROM dulieuphim WHERE MovieTitle LIKE %s OR STT LIKE %s"
        cursor.execute(query, ('%' + search_query + '%', '%' + search_query + '%'))
        # Lấy tất cả các dòng kết quả từ truy vấn
        rows = cursor.fetchall()
        # Hiển thị dữ liệu trên bảng dữ liệu phim   
        for row in rows:
            self.movie_table.insert('', 'end', values=row)
        # Đóng kết nối và cursor
        cursor.close()
        cnx.close()
    def save_film(self):
        # Kiểm tra xem các entry đã được điền đầy đủ hay chưa
        if any(not entry.get() for entry in self.entries):
            self.label_message.config(text="Vui lòng nhập đủ thông tin")
        else:
            # Lấy thông tin từ các phần nhập liệu
            film_info = {}
            for i, entry in enumerate(self.entries):
                film_info[self.labels[i]] = entry.get()

            try:
                # Kết nối tới cơ sở dữ liệu MySQL
                cnx = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="dinhan24092002",
                    database="finalproject"
                )

                # Tạo đối tượng cursor để thực hiện các truy vấn
                cursor = cnx.cursor()

                # Kiểm tra xem phim có tồn tại trong cơ sở dữ liệu hay không
                select_query = "SELECT * FROM dulieuphim WHERE MovieTitle = %s"
                cursor.execute(select_query, (film_info["Movie Title:"],))
                result = cursor.fetchone()

                if result:
                    # Nếu phim đã tồn tại, thực hiện truy vấn UPDATE để cập nhật thông tin
                    update_query = """
                    UPDATE dulieuphim
                    SET ReleaseDate = %s, Price = %s, Oder_number = %s, Revenue = %s, 
                        ProductionBudget = %s, WorldwideGross = %s, DomesticGross = %s
                    WHERE MovieTitle = %s
                    """
                    values = (
                        film_info["ReleaseDate:"],
                        film_info["Price:"],
                        film_info["Order Number:"],
                        film_info["Revenue:"],
                        film_info["Production Budget:"],
                        film_info["Worldwide Gross:"],
                        film_info["Domestic Gross:"],
                        film_info["Movie Title:"]
                    )
                    cursor.execute(update_query, values)
                else:
                    # Nếu phim chưa tồn tại, thực hiện truy vấn INSERT để lưu thông tin phim vào bảng dulieuphim
                    insert_query = "INSERT INTO dulieuphim (STT, ReleaseDate, MovieTitle, Price, Oder_number, Revenue, ProductionBudget, WorldwideGross, DomesticGross) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s)"
                    values = (
                        film_info["ReleaseDate:"],
                        film_info["Movie Title:"],
                        film_info["Price:"],
                        film_info["Order Number:"],
                        film_info["Revenue:"],
                        film_info["Production Budget:"],
                        film_info["Worldwide Gross:"],
                        film_info["Domestic Gross:"]
                    )
                    cursor.execute(insert_query, values)

                # Lưu các thay đổi vào cơ sở dữ liệu
                cnx.commit()

                # Đóng kết nối và cursor
                cursor.close()
                cnx.close()

                # Sau khi lưu thành công, thông báo cho người dùng và xóa dữ liệu các entry
                self.label_message.config(text="Lưu thành công")
                for entry in self.entries:
                    entry.delete(0, tk.END)
            except mysql.connector.Error as error:
                print("Lỗi khi kết nối và lưu dữ liệu vào MySQL:", error)
                self.label_message.config(text="Lưu thất bại")
    def delete_film(self):
        film_name_or_order = self.entry_delete.get()

        try:
            # Kết nối tới cơ sở dữ liệu MySQL
            cnx = mysql.connector.connect(
                host="localhost",
                user="root",
                password="dinhan24092002",
                database="finalproject"
            )

            # Tạo đối tượng cursor để thực hiện các truy vấn
            cursor = cnx.cursor()

            # Kiểm tra xem film_name_or_order có phải là số hay không
            if film_name_or_order.isdigit():
                # Xóa phim dựa trên STT
                delete_query = "DELETE FROM dulieuphim WHERE STT = %s"
                cursor.execute(delete_query, (film_name_or_order,))
            else:
                # Xóa phim dựa trên tên phim
                delete_query = "DELETE FROM dulieuphim WHERE MovieTitle = %s"
                cursor.execute(delete_query, (film_name_or_order,))

            # Lưu các thay đổi vào cơ sở dữ liệu
            cnx.commit()

            # Đóng kết nối và cursor
            cursor.close()
            cnx.close()

            # Xóa dữ liệu nhập trong entry
            self.entry_delete.delete(0, tk.END)

            # Hiển thị thông báo xóa thành công
            self.label_message.config(text="Xóa thành công")
        except mysql.connector.Error as error:
            print("Lỗi khi kết nối và xóa dữ liệu trong MySQL:", error)
class PriceFrame:
    def __init__(self, parent):
        self.parent = parent

        # Tạo frame chứa nội dung Đơn hàng
        self.price_film_frame = tk.Frame(self.parent.content_frame)
        self.price_film_frame.pack(fill=tk.BOTH, expand=True)

        # Tạo frame con bên trái để hiển thị bảng dữ liệu phim và thanh cuộn
        left_frame = tk.Frame(self.price_film_frame,width=400, height=800)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        # Giới hạn kích thước của left_frame
        left_frame.pack_propagate(False)    

        # Tạo ô tìm kiếm
        search_button = tk.Button(left_frame, text="Tìm kiếm",bg='khaki', command=self.search_movies)
        search_button.pack()

        self.search_entry = tk.Entry(left_frame)
        self.search_entry.pack()

        # Tạo thanh cuộn
        scrollbar = tk.Scrollbar(left_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Tạo thanh cuộn ngang
        xscrollbar = tk.Scrollbar(left_frame, orient=tk.HORIZONTAL)
        xscrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        # Tạo bảng dữ liệu phim
        self.movie_table = ttk.Treeview(left_frame, yscrollcommand=scrollbar.set)
        # Thêm các cột và dữ liệu vào bảng dữ liệu phim
        self.movie_table['columns'] = ('STT', 'ReleaseDate', 'MovieTitle', 'Price','Order_number','Revenue')

        self.movie_table.heading('STT', text='STT')
        self.movie_table.heading('ReleaseDate', text='ReleaseDate')
        self.movie_table.heading('MovieTitle', text='MovieTitle')
        self.movie_table.heading('Price', text='Price')
        self.movie_table.heading('Order_number', text='Order_number')
        self.movie_table.heading('Revenue', text='Revenue')

        # Tìm index của cột "MovieTitle"
        column_index = self.movie_table['columns'].index('MovieTitle')
        # Tính toán vị trí cuộn ngang của thanh cuộn
        scroll_position = column_index / len(self.movie_table['columns'])

        # Di chuyển thanh cuộn ngang đến vị trí mong muốn
        self.movie_table.xview_moveto(scroll_position)

        # Kết nối thanh cuộn với bảng dữ liệu phim
        scrollbar.config(command=self.movie_table.yview)
        # Kết nối thanh cuộn ngang với bảng dữ liệu phim
        self.movie_table.configure(xscrollcommand=xscrollbar.set)
        xscrollbar.config(command=self.movie_table.xview)

        # Hiển thị bảng dữ liệu phim
        self.movie_table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Gọi hàm để hiển thị dữ liệu phim từ MySQL
        self.load_movies()

        # Tạo frame con bên phải để hiển thị thông tin phim và các tùy chọn khác
        right_frame = tk.Frame(self.price_film_frame)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        # Giới hạn kích thước của left_frame
        right_frame.pack_propagate(False) 
        # Thêm nội dung mới vào frame bên phải
        label = tk.Label(right_frame, text="Thông tin phim")
        label.pack()

        # Tạo các label để hiển thị thông tin phim
        self.label_stt = tk.Label(right_frame, text="STT:",anchor="w")
        self.label_stt.pack(anchor="w")
        self.label_release_date = tk.Label(right_frame, text="Ngày phát hành:",anchor="w")
        self.label_release_date.pack(anchor="w")
        self.label_movie_title = tk.Label(right_frame, text="Tên phim:",anchor="w")
        self.label_movie_title.pack(anchor="w")
        self.label_price = tk.Label(right_frame, text="Đơn giá:",anchor="w")
        self.label_price.pack(anchor="w")
        self.label_order_number = tk.Label(right_frame, text="Số lượng đặt:",anchor="w")
        self.label_order_number.pack(anchor="w")
        self.label_revenue = tk.Label(right_frame, text="Doanh thu:",anchor="w")
        self.label_revenue.pack(anchor="w")

        # Tạo phần nhập liệu cho tên hoặc số thứ tự phim cần xóa trong frame Xóa phim
        self.label_change = tk.Label(right_frame, text="Đơn giá mới:")
        self.label_change.pack(padx=10, pady=5)

        self.entry_change = tk.Entry(right_frame)
        self.entry_change.pack(padx=10, pady=5)

        button_change = tk.Button(right_frame, text="Thay đổi",bg='silver', command=self.change_price)
        button_change.pack(padx=10, pady=5)
        self.error_label = tk.Label(right_frame, text="")
        self.error_label.pack()
    def load_movies(self):
        # Kết nối tới cơ sở dữ liệu MySQL
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="dinhan24092002",
            database="finalproject"
        )
        cursor = cnx.cursor()

        # Truy vấn dữ liệu từ bảng dulieuphim trong MySQL
        query = "SELECT * FROM dulieuphim"
        cursor.execute(query)

        # Lấy tất cả các dòng kết quả từ truy vấn
        rows = cursor.fetchall()

        # Hiển thị dữ liệu trên bảng dữ liệu phim
        for row in rows:
            self.movie_table.insert('', 'end', values=row)

        # Đóng kết nối và cursor
        cursor.close()
        cnx.close()
    def search_movies(self):
        # Xóa nội dung hiện tại của bảng dữ liệu phim
        self.movie_table.delete(*self.movie_table.get_children())
        # Lấy từ khóa tìm kiếm từ entry
        search_query = self.search_entry.get()
        # Kết nối tới cơ sở dữ liệu MySQL
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="dinhan24092002",
            database="finalproject"
        )
        cursor = cnx.cursor()
        # Truy vấn dữ liệu phim từ MySQL dựa trên từ khóa tìm kiếm
        query = "SELECT * FROM dulieuphim WHERE MovieTitle LIKE %s OR STT LIKE %s"
        cursor.execute(query, ('%' + search_query + '%', '%' + search_query + '%'))
        # Lấy tất cả các dòng kết quả từ truy vấn
        rows = cursor.fetchall()
        # Hiển thị dữ liệu trên bảng dữ liệu phim   
        for row in rows:
            self.movie_table.insert('', 'end', values=row)
        # Đóng kết nối và cursor
        cursor.close()
        cnx.close()
        # Gắn sự kiện chọn dòng trong bảng dữ liệu phim
        self.movie_table.bind("<<TreeviewSelect>>", self.update_movie_info)
    def update_movie_info(self, event):
        # Xóa nội dung hiện tại của phần frame "Thông tin phim"
        self.clear_movie_info()

        # Lấy thông tin phim từ dòng được chọn trong bảng dữ liệu phim
        selected_item = self.movie_table.focus()
        movie_info = self.movie_table.item(selected_item, 'values')

        # Hiển thị thông tin phim trong frame "Thông tin phim"
        self.label_stt.config(text="STT: " + str(movie_info[0]))
        self.label_release_date.config(text="Ngày phát hành: " + str(movie_info[1]))
        self.label_movie_title.config(text="Tên phim: " + str(movie_info[2]))
        self.label_price.config(text="Đơn giá: " + str(movie_info[3]))
        self.label_order_number.config(text="Số lượng đặt: " + str(movie_info[4]))
        self.label_revenue.config(text="Doanh thu: " + str(movie_info[5]))

    def clear_movie_info(self):
        # Xóa nội dung của các label trong phần frame "Thông tin phim"
        self.label_stt.config(text="STT:")
        self.label_release_date.config(text="Ngày phát hành:")
        self.label_movie_title.config(text="Tên phim:")
        self.label_price.config(text="Đơn giá:")
        self.label_order_number.config(text="Số lượng đặt:")
        self.label_revenue.config(text="Doanh thu:")
    def change_price(self):
        try:
            # Lấy giá trị mới từ entry
            new_price = self.entry_change.get()

            # Lấy thông tin phim từ dòng được chọn trong bảng dữ liệu phim
            selected_item = self.movie_table.focus()
            movie_info = self.movie_table.item(selected_item, 'values')

            # Lấy giá trị hiện tại của cột Price
            current_price = movie_info[3]

            if not  new_price :
                # Chưa nhập đủ thông tin
                self.error_label.config(text="Lỗi: Vui lòng nhập đủ thông tin.",fg="red")
                return
            # Kiểm tra nếu giá trị mới khác giá trị hiện tại
            if new_price != current_price:
                # Lấy STT của phim
                stt = movie_info[0]

                # Kết nối tới cơ sở dữ liệu MySQL
                cnx = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="dinhan24092002",
                    database="finalproject"
                )
                cursor = cnx.cursor()

                # Cập nhật giá trị mới vào cơ sở dữ liệu
                update_query = "UPDATE dulieuphim SET Price = %s WHERE STT = %s"
                cursor.execute(update_query, (new_price, stt))
                cnx.commit()
                self.error_label.config(text="Thay đổi thành công",fg="red")
                # Đóng kết nối và cursor
                cursor.close()
                cnx.close()

                # Cập nhật lại thông tin phim sau khi thay đổi giá
                self.update_movie_info(None)
        except:
            # Xóa dữ liệu nhập trong entry
            self.entry_change.delete(0, tk.END)

            # Hiển thị thông báo xóa thành công
            self.error_label.config(text="Lỗi: Vui lòng nhập đủ thông tin.",fg="red")
class TicketFrame:
    def __init__(self, parent):
        self.parent = parent
        # Tạo frame chứa nội dung Đơn hàng
        self.price_film_frame = tk.Frame(self.parent.content_frame)
        self.price_film_frame.pack(fill=tk.BOTH, expand=True)

        # Tạo frame con bên trái để hiển thị bảng dữ liệu phim và thanh cuộn
        left_frame = tk.Frame(self.price_film_frame,width=400, height=800)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        # Giới hạn kích thước của left_frame
        left_frame.pack_propagate(False)    

        # Tạo ô tìm kiếm
        search_button = tk.Button(left_frame, text="Tìm kiếm",bg='khaki', command=self.search_movies)
        search_button.pack()

        self.search_entry = tk.Entry(left_frame)
        self.search_entry.pack()

        # Tạo thanh cuộn
        scrollbar = tk.Scrollbar(left_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Tạo thanh cuộn ngang
        xscrollbar = tk.Scrollbar(left_frame, orient=tk.HORIZONTAL)
        xscrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        # Tạo bảng dữ liệu phim
        self.movie_table = ttk.Treeview(left_frame, yscrollcommand=scrollbar.set)
        # Thêm các cột và dữ liệu vào bảng dữ liệu phim
        self.movie_table['columns'] = ('STT', 'ReleaseDate', 'MovieTitle', 'Price','Order_number','Revenue')

        self.movie_table.heading('STT', text='STT')
        self.movie_table.heading('ReleaseDate', text='ReleaseDate')
        self.movie_table.heading('MovieTitle', text='MovieTitle')
        self.movie_table.heading('Price', text='Price')
        self.movie_table.heading('Order_number', text='Order_number')
        self.movie_table.heading('Revenue', text='Revenue')

        # Tìm index của cột "MovieTitle"
        column_index = self.movie_table['columns'].index('MovieTitle')
        # Tính toán vị trí cuộn ngang của thanh cuộn
        scroll_position = column_index / len(self.movie_table['columns'])

        # Di chuyển thanh cuộn ngang đến vị trí mong muốn
        self.movie_table.xview_moveto(scroll_position)

        # Kết nối thanh cuộn với bảng dữ liệu phim
        scrollbar.config(command=self.movie_table.yview)
        # Kết nối thanh cuộn ngang với bảng dữ liệu phim
        self.movie_table.configure(xscrollcommand=xscrollbar.set)
        xscrollbar.config(command=self.movie_table.xview)

        # Hiển thị bảng dữ liệu phim
        self.movie_table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Gọi hàm để hiển thị dữ liệu phim từ MySQL
        self.load_movies()

        # Tạo frame con bên phải để hiển thị thông tin phim và các tùy chọn khác
        right_frame = tk.Frame(self.price_film_frame)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        # Giới hạn kích thước của left_frame
        right_frame.pack_propagate(False) 
        # Thêm nội dung mới vào frame bên phải
        label = tk.Label(right_frame, text="Thông tin phim")
        label.pack()

        # Tạo các label để hiển thị thông tin phim
        self.label_stt = tk.Label(right_frame, text="STT:",anchor="w")
        self.label_stt.pack(anchor="w")
        self.label_release_date = tk.Label(right_frame, text="Ngày phát hành:",anchor="w")
        self.label_release_date.pack(anchor="w")
        self.label_movie_title = tk.Label(right_frame, text="Tên phim:",anchor="w")
        self.label_movie_title.pack(anchor="w")
        self.label_price = tk.Label(right_frame, text="Đơn giá:",anchor="w")
        self.label_price.pack(anchor="w")
        self.label_order_number = tk.Label(right_frame, text="Số lượng đặt:",anchor="w")
        self.label_order_number.pack(anchor="w")
        
        # Tạo phần nhập liệu cho tên hoặc số thứ tự phim cần xóa trong frame Xóa phim
        self.label_number = tk.Label(right_frame, text="Số Lượng vé:")
        self.label_number.pack(padx=10, pady=5)

        self.entry_number = tk.Entry(right_frame)
        self.entry_number.pack(padx=3, pady=1)

        button_plus = tk.Button(right_frame, text="Đặt",bg='silver', command=self.Order)
        button_plus.pack(padx=10, pady=5)
        self.error_label = tk.Label(right_frame, text="")
        self.error_label.pack()
    def load_movies(self):
        # Kết nối tới cơ sở dữ liệu MySQL
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="dinhan24092002",
            database="finalproject"
        )
        cursor = cnx.cursor()

        # Truy vấn dữ liệu từ bảng dulieuphim trong MySQL
        query = "SELECT * FROM dulieuphim"
        cursor.execute(query)

        # Lấy tất cả các dòng kết quả từ truy vấn
        rows = cursor.fetchall()

        # Hiển thị dữ liệu trên bảng dữ liệu phim
        for row in rows:
            self.movie_table.insert('', 'end', values=row)

        # Đóng kết nối và cursor
        cursor.close()
        cnx.close()
    def search_movies(self):
        # Xóa nội dung hiện tại của bảng dữ liệu phim
        self.movie_table.delete(*self.movie_table.get_children())
        # Lấy từ khóa tìm kiếm từ entry
        search_query = self.search_entry.get()
        # Kết nối tới cơ sở dữ liệu MySQL
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="dinhan24092002",
            database="finalproject"
        )
        cursor = cnx.cursor()
        # Truy vấn dữ liệu phim từ MySQL dựa trên từ khóa tìm kiếm
        query = "SELECT * FROM dulieuphim WHERE MovieTitle LIKE %s OR STT LIKE %s"
        cursor.execute(query, ('%' + search_query + '%', '%' + search_query + '%'))
        # Lấy tất cả các dòng kết quả từ truy vấn
        rows = cursor.fetchall()
        # Hiển thị dữ liệu trên bảng dữ liệu phim   
        for row in rows:
            self.movie_table.insert('', 'end', values=row)
        # Đóng kết nối và cursor
        cursor.close()
        cnx.close()
        # Gắn sự kiện chọn dòng trong bảng dữ liệu phim
        self.movie_table.bind("<<TreeviewSelect>>", self.update_movie_info)
    def update_movie_info(self, event):
        # Xóa nội dung hiện tại của phần frame "Thông tin phim"
        self.clear_movie_info()

        self.number_ticket=self.entry_number.get()
        
        # Lấy thông tin phim từ dòng được chọn trong bảng dữ liệu phim
        selected_item = self.movie_table.focus()
        movie_info = self.movie_table.item(selected_item, 'values')

        
        # Hiển thị thông tin phim trong frame "Thông tin phim"
        self.label_stt.config(text="STT: " + str(movie_info[0]))
        self.label_release_date.config(text="Ngày phát hành: " + str(movie_info[1]))
        self.label_movie_title.config(text="Tên phim: " + str(movie_info[2]))
        self.label_price.config(text="Đơn giá: " + str(movie_info[3]))
        self.label_order_number.config(text="Số lượng đặt: " + self.number_ticket)
        self.Tong_gia=int(movie_info[3])*int(self.number_ticket)

    def Order(self):
        dong1="-------------MOVIE TICKET-------------"
        dong2="DATE:                          9/6/2022"
        dong3="CASHIER:                 Hoàng Đình An"
        dong4="-------------FILM DETAILS-------------"
        dong8="--------------------------------------"
        dong9="TỔNG GIÁ: "+ str(self.Tong_gia)
        noi_dung = dong1+'\n'+dong2+'\n'+dong3+'\n'+dong4+'\n'+self.label_movie_title.cget("text") + '\n' + self.label_price.cget("text") + '\n' + self.label_order_number.cget("text")+'\n'+dong8+'\n'+dong9
        with open("E:\APEN FINAL\\BILL.txt", "w", encoding="utf-8") as file:
            file.write(noi_dung)
    def clear_movie_info(self):
        # Xóa nội dung của các label trong phần frame "Thông tin phim"
        self.label_stt.config(text="STT:")
        self.label_release_date.config(text="Ngày phát hành:")
        self.label_movie_title.config(text="Tên phim:")
        self.label_price.config(text="Đơn giá:")
        self.label_order_number.config(text="Số lượng đặt:")
        


class AccountFrame:
    def __init__(self, parent, username):
        self.parent = parent
        self.username = username


        # Hiển thị mật khẩu
        self.show_password = tk.BooleanVar()
        self.show_password.set(False)
        # Tạo frame chứa nội dung
        self.show_account_frame = tk.Frame(self.parent.content_frame)
        self.show_account_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.show_account_frame.pack_propagate(False)
        # Tạo frame chứa nội dung thay đổi mật khẩu
        self.change_password_frame = tk.Frame(self.parent.content_frame)
        self.change_password_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.change_password_frame.pack_propagate(False)
        # Tạo các nhãn và ô nhập mật khẩu cũ
        old_password_label = tk.Label(self.change_password_frame, text="Old Password:")
        old_password_label.pack()

        self.old_password_entry = tk.Entry(self.change_password_frame, show="*")
        self.old_password_entry.pack()

        # Tạo các nhãn và ô nhập mật khẩu mới
        new_password_label = tk.Label(self.change_password_frame, text="New Password:")
        new_password_label.pack()

        self.new_password_entry = tk.Entry(self.change_password_frame, show="*")
        self.new_password_entry.pack()

        # Tạo các nhãn và ô nhập lại mật khẩu mới
        confirm_password_label = tk.Label(self.change_password_frame, text="Confirm Password:")
        confirm_password_label.pack()

        self.confirm_password_entry = tk.Entry(self.change_password_frame, show="*")
        self.confirm_password_entry.pack()

        button_change = tk.Button(self.change_password_frame, text="Thay đổi",bg='silver', command=self.change_password)
        button_change.pack(padx=10, pady=5)
        self.checkbutton_show_password = tk.Checkbutton(self.change_password_frame, text="Hiển thị mật khẩu",variable=self.show_password,command=self.toggle_password_visibility)
        self.checkbutton_show_password.pack()
        self.error_label = tk.Label(self.change_password_frame, text="",fg="red")
        self.error_label.pack()
        # Kết nối tới cơ sở dữ liệu MySQL
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="dinhan24092002",
            database="finalproject"
        )

        cursor = cnx.cursor()

        # Truy vấn dữ liệu từ bảng users trong MySQL dựa trên username
        query = "SELECT username, id FROM users WHERE username = %s"
        cursor.execute(query, (self.username,))

        # Lấy dòng kết quả từ truy vấn
        row = cursor.fetchone()

        if row is not None:
            username_label = tk.Label(self.show_account_frame, text="Username: " + str(row[0]))
            username_label.pack()

            id_label = tk.Label(self.show_account_frame, text="ID: " + str(row[1]))
            id_label.pack()

        cursor.close()
        cnx.close()
    def change_password(self):
        # Kết nối tới cơ sở dữ liệu MySQL
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="dinhan24092002",
            database="finalproject"
        )

        cursor = cnx.cursor()

        # Truy vấn dữ liệu mật khẩu hiện tại từ bảng users trong MySQL dựa trên username
        query = "SELECT password FROM users WHERE username = %s"
        cursor.execute(query, (self.username,))

        # Lấy mật khẩu hiện tại từ kết quả truy vấn
        current_password = cursor.fetchone()[0]

        # Đóng kết nối cơ sở dữ liệu
        cursor.close()
        cnx.close()

        # Lấy mật khẩu mới và xác nhận mật khẩu từ các ô nhập
        old_password = self.old_password_entry.get()
        new_password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        # Kiểm tra xem người dùng đã nhập đủ thông tin hay chưa
        if not old_password or not new_password or not confirm_password:
            # Chưa nhập đủ thông tin
            self.error_label.config( text="Lỗi: Vui lòng nhập đủ thông tin.",fg="red")
            return

        # Kiểm tra xem mật khẩu cũ có trùng khớp hay không
        if old_password != current_password:
            # Mật khẩu cũ không trùng khớp
            self.error_label.config( text="Lỗi: Mật khẩu cũ không chính xác.",fg="red")
            return

        # Kiểm tra xem mật khẩu mới và xác nhận mật khẩu có trùng khớp hay không
        if new_password != confirm_password:
            # Mật khẩu mới và mật khẩu xác nhận không trùng khớp
            self.error_label.config( text="Lỗi: Mật khẩu xác nhận không khớp.",fg="red")
            return

        # Kết nối lại tới cơ sở dữ liệu MySQL
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="dinhan24092002",
            database="finalproject"
        )

        cursor = cnx.cursor()

        # Cập nhật mật khẩu mới vào cơ sở dữ liệu
        update_query = "UPDATE users SET password = %s WHERE username = %s"
        cursor.execute(update_query, (new_password, self.username))
        cnx.commit()

        # Đóng kết nối cơ sở dữ liệu
        cursor.close()
        cnx.close()

        # Mật khẩu cũ trùng khớp và mật khẩu mới trùng khớp
        self.error_label.config( text="Thay đổi mật khẩu thành công.")

        # Xóa nội dung trong các trường nhập mật khẩu
        self.old_password_entry.delete(0, tk.END)
        self.new_password_entry.delete(0, tk.END)
        self.confirm_password_entry.delete(0, tk.END)
    # Hàm hiện mật khẩu
    def toggle_password_visibility(self):
        if self.show_password.get():
            self.old_password_entry.config(show="")
            self.new_password_entry.config(show="")
            self.confirm_password_entry.config(show="")
        else:
            self.old_password_entry.config(show="")
            self.new_password_entry.config(show="*")
            self.confirm_password_entry.config(show="*")
#%%
# Tạo đối tượng cửa sổ đăng nhập và chạy ứng dụng
login_window = LoginWindow()
login_window.run()