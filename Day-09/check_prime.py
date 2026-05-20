#check prime using while loop
n = int(input("enter number here:"))
i = 2
flag = 0

while i < n:
    if n % i == 0:
        flag = 1
        break
    i += 1

if flag == 0:
    print("Prime")
else:
    print("Not Prime")
