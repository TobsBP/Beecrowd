firt_input = input().split()
second_input = input().split()

data = [
    {"code": int(firt_input[0]), "quantity": int(firt_input[1]), "unit_price": float(firt_input[2])},
    {"code": int(second_input[0]), "quantity": int(second_input[1]), "unit_price": float(second_input[2])},
]

total = data[0]["quantity"] * data[0]["unit_price"] + data[1]["quantity"] * data[1]["unit_price"]

print(f"VALOR A PAGAR: R$ {total:.2f}")
