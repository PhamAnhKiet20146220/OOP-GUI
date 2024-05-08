#bai4
class Time():    
    def __init__(self, giay):
        self.giay = giay
    def convert_to_minutes(self):
        self.minutes = self.giay // 60
        self.second = self.giay - (self.minutes*60)
        return str(self.minutes)+":" + str(self.second)
    def convert_to_hours(self):
        self.hour = self.giay//3600
        self.minutes = (self.giay - (self.hour*3600))//60
        self.second = self.giay - (self.minutes*60) - (self.hour*3600)
        return str(self.hour)+':'+str(self.minutes)+':' +str(self.second)
thoigian = Time(230)
print(thoigian.convert_to_minutes())
print(thoigian.convert_to_hours())
