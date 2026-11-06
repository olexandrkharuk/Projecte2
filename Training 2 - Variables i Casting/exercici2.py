num1 = int(input("Introdueix el primer nombre: "))
num2 = int(input("Introdueix el segon nombre: "))

print("Suma:", num1 + num2)
print("Resta:", num1 - num2)
print("Multiplicació:", num1 * num2)

if num2 != 0:
    print("Divisió:", num1 / num2)
else:
    print("No es pot dividir entre zero")
