def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ошибка: деление на ноль!"
    return x / y

print("Простой калькулятор")
print("Выберите операцию:")
print("1. Сложение (+)")
print("2. Вычитание (-)")
print("3. Умножение (*)")
print("4. Деление (/)")

choice = input("Введите номер операции (1/2/3/4) или символ (+, -, *, /): ").strip()

# Преобразуем символы в номера для удобства
if choice == '+':
    choice = '1'
elif choice == '-':
    choice = '2'
elif choice == '*':
    choice = '3'
elif choice == '/':
    choice = '4'

if choice in ('1', '2', '3', '4'):
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка: введите корректные числа!")
        exit()

    if choice == '1':
        print(f"Результат: {num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"Результат: {num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"Результат: {num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        result = divide(num1, num2)
        print(f"Результат: {num1} / {num2} = {result}")
else:
    print("Неверный выбор операции!")
