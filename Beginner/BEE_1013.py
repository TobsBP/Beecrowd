input = input().split()

a = int(input[0])
b = int(input[1])
c = int(input[2])

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print(f"{largest} eh o maior")