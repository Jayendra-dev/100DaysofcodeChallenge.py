# To check whether the number is perfect or not
# LOGIC:jo number apne divisors ka sum ho.Khud ko chhhod ke.
# First  4 perfectg no.6/    1+2+3=6,28/     1+2+4+7+14=  28,     496,    8128
n = int(input("enter a no.Here:))
i = 1
sum = 0

while i < n:
    if n % i == 0:
        sum += i
    i += 1

if sum == n:
    print("Perfect Number")
else:
    print("Not Perfect")
