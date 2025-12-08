money = int(input())

notes = [100, 50, 20, 10, 5, 2, 1]

print(f"{money}")
print(f"{money // 100} nota(s) de R$ 100,00")
money = money % 100
print(f"{money // 50} nota(s) de R$ 50,00")
money = money % 50
print(f"{money // 20} nota(s) de R$ 20,00")
money = money % 20
print(f"{money // 10} nota(s) de R$ 10,00")
money = money % 10
print(f"{money // 5} nota(s) de R$ 5,00")
money = money % 5
print(f"{money // 2} nota(s) de R$ 2,00")
money = money % 2
print(f"{money // 1} nota(s) de R$ 1,00")
