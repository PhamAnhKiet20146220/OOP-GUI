class Investment:
    def __init__(self, p, i):
        self.p = p
        self.i = i
    def value_after(self, n):
        P = (self.p*( 1 + self.i/100)**n)
        print("after",n,"years, you have",P,"dolla")
    def _str_(self):
        print("Pro")