# program to handle division by zero
try:
    a=int(input("enter numerator: "))
    b=int(input("enter denominator:"))
    result=a/b
    print("result:",result)
except ZeroDivisionError:
    print("division by zero is not allowed")
