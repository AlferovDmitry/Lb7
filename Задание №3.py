#3. Запросите у пользователя целое неотрицательное число и вычислите его факториал. Факториал числа n, вычисляется как n! = 1 × 2 × 3 × … × n.

#Решение

num = int(input("Введите целое неотрицательное число: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Факториал числа", num, "равен", factorial)

#Итог
#Введите целое неотрицательное число:
#2
#Факториал числа 2 равен 2

