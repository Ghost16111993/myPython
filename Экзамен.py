# Калькулятор
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
operation = input("Введите номер операции (1/2/3/4): ")
if operation == "1":
    result = num1 + num2
elif operation == "2":
    result = num1 - num2
elif operation == "3":
    result = num1 * num2
elif operation == "4":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Ошибка: деление на ноль!"
else:
    result = "Ошибка: некорректная операция."
print(f"Результат: {result}")

# НОД
import math
num1 = 50
num2 = 10
gcd_result = math.gcd(num1, num2)
print(f"НОД({num1}, {num2}) = {gcd_result}")


