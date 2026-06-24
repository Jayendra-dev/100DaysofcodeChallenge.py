#Handle invalid conversion
try:
    num=int(input("enter character:"))
    result=12/num
    print("result:",result)
except ValueError:
    print("input invalid,, please enter integer value")    