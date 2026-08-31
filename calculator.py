print("Простой калькулятор")

a = float(input("Первое число: "))
operation = input("Операция (+, -, *, /): ")
b = float(input("Второе число: "))

if operation == "+":
    result = a + b
elif operation == "-":
    result = a - b
elif operation == "*":
    result = a * b
elif operation == "/":
    result = a / b
else:
    result = "Неизвестная операция"

print("Результат:", result)