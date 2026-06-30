# Difference between class variable and instance variable
class Employee:
    company="Google"  #class variable 
    def __init__(self,name):
        self.name=name     # instance variable
e1=Employee("Aman")
e2=Employee("Rohit")
print(e1.company)
print(e2.name) 


# output
#Google
#Rohit