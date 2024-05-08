class student():
    def __init__(self, name, StID, sex):
        self.name = name
        self.StID = StID
        self.sex = sex
        self.status = " ngủ"
    def greeting(self):
        print("Hello" , self.name)
        print("Hi", self.StID)
        print("a", self.sex)
    def cal(self, mid, final):
        self.Grade = ( mid + final)/2
        print("student ID", self.StID)
        print("điểm:", self.Grade)
        
Student01 = student("Cuong", "20164003", "M")
Student02 = student("Danh", "20164004", "N")
Student03 = student("Minh", "20164005", "M")
print(Student01.name)
print(Student02.StID)
print(Student03.sex)
print("greeting")
Student01.greeting()
Student02.greeting()
Student03.greeting()
print("status",Student01.status)
Student01.cal(5, 6)
print(Student01.Grade)
