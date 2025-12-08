input = input().split()

a = float(input[0])
b = float(input[1])
c = float(input[2])

area_triangle = (a * c) / 2
area_circle = 3.14159 * c**2
area_trapezoid = ((a + b) * c) / 2
area_square = b**2
area_rectangle = a * b

print(f"TRIANGULO: {area_triangle:.3f}")
print(f"CIRCULO: {area_circle:.3f}")
print(f"TRAPEZIO: {area_trapezoid:.3f}")
print(f"QUADRADO: {area_square:.3f}")
print(f"RETANGULO: {area_rectangle:.3f}")