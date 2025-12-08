n, x = map(int, input().split())
titan_sizes = input().strip()
p, m, g = map(int, input().split())

size_map = {'P': p, 'M': m, 'G': g}

walls_count = 1
remaining = x

for t in titan_sizes:
    k = size_map[t]

    if remaining >= k:
        remaining -= k
    else:
        walls_count += 1
        remaining = x - k

print(walls_count)
