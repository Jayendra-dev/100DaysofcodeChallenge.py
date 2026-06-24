# write a program using generic exception handling
try:
    num= int(input("enter a number:"))
    print(10/num)
except Exception as e:
    print("error occured:",e)