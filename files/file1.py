import math

try:
    num = float(input("Введите число, чтобы найти его квадратный корень: "))
    if num < 0:
        print("Квадратный корень из отрицательного числа не определён в вещественных числах.")
    else:
        sqrt_result = math.sqrt(num)
        print(f"Квадратный корень из {num} равен {sqrt_result}")
except ValueError:
    print("Пожалуйста, введите корректное числовое значение.")
