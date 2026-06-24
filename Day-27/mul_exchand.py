try:
    a=int(input("enter numerator :"))
    b=int(input("enter denominator:"))
    result=a/b
    print('result:',result)
except ValueError:
    print("enter correct  value.enter integers only ")
except ZeroDivisionError:
    print("enter other than zero")

