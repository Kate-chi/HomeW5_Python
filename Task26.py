# Задача 26:
# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии

A = int(input("Введите число А: "))
B = int(input("Введите число B: "))

def degree(a, b):
    if b == 1:
        return a
    elif b == 0:
        return 1
    else:
        return a * degree(a, b-1)
    
print(degree(A, B))