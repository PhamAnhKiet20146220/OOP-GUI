import matplotlib.pyplot as plt
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def plot_point(self):
        plt.pilot(self.x,self.y,'ro')
        plt.show()
        
    def cal_dist(self,x,y):
        dist = ((self.x-x)**2+(self.y-y)**2)**0.5
        print(dist)
A = Point(10,20)
B = Point(0,0)
A.cal_dist(0, 15)


