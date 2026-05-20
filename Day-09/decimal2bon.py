# convert Decimal to binary
n = int(input("enter the decimal number to change in binary:"))
binary = ""

while n > 0:
    binary = str(n % 2) + binary
    n //= 2

print(binary)
