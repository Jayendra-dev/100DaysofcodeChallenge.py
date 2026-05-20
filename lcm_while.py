# Find lcm using while loop
a = int(input("enter your first number here:"))
b = int(input("enter your second number here:"))

max_num = max(a, b)

while True:
    if max_num % a == 0 and max_num % b == 0:
        print(max_num)
        break
    max_num += 1
