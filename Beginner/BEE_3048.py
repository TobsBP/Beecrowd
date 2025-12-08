size = int(input())
sequence = []

for _ in range(size):
    sequence.append(int(input()))

count = 1

for i in range(1, size):
    if sequence[i] != sequence[i - 1]:
        count += 1

print(count)
