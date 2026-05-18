# print factorial in python using while loop.
n = int(input("enter no.  to find factorial of a no.:"))
fact = 1

while n > 0:
    fact *= n
    n -= 1

print(fact)

print("/n")
# reverse a number
n = int(input("ente no. to reverse ,for ex.7645:"))
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

print(rev)

print("/n")
# Check palindrome number using while loop.
n = int(input( "enter a number here to check palindrome:"))
temp = n
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")


# count  digit in a number
n = int(input("enter no. to count digits:"))
count = 0

while n > 0:
    count += 1
    n //= 10

print(count)


# sum of digits of a number
n = int(input( "enter no. here to find sum of digits:"))
sum = 0

while n > 0:
    sum += n % 10
    n //= 10

print(sum)


