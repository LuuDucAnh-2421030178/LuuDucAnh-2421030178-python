class circle:
    pi = 3.141592
    def __init__(self, radius=1):
        self.bk = radius
    def dientich(self):
        return self.bk * self.bk * circle.pi
c = circle(5)
print("dien tich hinh tron la:", c.dientich())