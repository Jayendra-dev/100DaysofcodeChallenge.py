# use of else statement in exception handling
try:
    num=int(input("enter number:"))
    result=100/num
except ZeroDivisionError:
    print("cannot divide by zero")
else:
    print("Division successful :",result)        