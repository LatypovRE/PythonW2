#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:
#- 6782 -> 23
#- 0,56 -> 11


# x = int (input('Введите вещентственное число: ')) Данное решение нашел в интернете
#print(sum(map(int, list(input()))))

x = float(input('Введите вещентственное число: ')) # Не могу понять что не так делаю
def num (x):
    for i in x:
        if i <= len(x):
            return i+1
        else:
            return 
print(num)
