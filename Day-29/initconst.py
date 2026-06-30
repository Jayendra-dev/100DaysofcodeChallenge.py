# init constructor intialises object data automatically
class Car:
    def __init__(self,brand):
        self.brand=brand
c1=Car("BMW")
print(c1.brand)        
