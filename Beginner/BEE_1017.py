autonomy = 12

time = int(input())
speed = int(input())

distance = time * speed

liters = distance / autonomy

print(f"{liters:.3f}")