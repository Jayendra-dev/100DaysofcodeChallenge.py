# Check Strong No.
# Hint: 145=1!+2!+5!=145---ye strong no. h
n = int(input("enter NO. Here :"))
temp = n
sum = 0

while n > 0:
    digit = n % 10

    fact = 1
    i = 1
    while i <= digit:
        fact *= i
        i += 1

    sum += fact
    n //= 10

if temp == sum:
    print("Strong Number")
else:
    print("Not Strong")
