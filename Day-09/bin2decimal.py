# convert binary to decimal.
binary = int(input( "enter binary number here:"))

power = 0
decimal = 0

while binary > 0:
    digit = binary % 10
    decimal += digit * (2 ** power)
    power += 1
    binary //= 10

print(decimal)
