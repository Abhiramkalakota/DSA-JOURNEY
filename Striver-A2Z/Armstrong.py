n = int(input())
temp = n
total = 0

while n > 0:
    digit = n % 10
    total += digit ** 3
    n //= 10

if total == temp:
    print("Armstrong")
else:
    print("Not Armstrong")