import math

def square(num):
    return  math.ceil(num * num)
num =  float(input('Сторона квадрата равна: '))
result = square(num)
print(f'Площадь квадрата равна - {square(num)}')