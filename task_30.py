a1 = int(input('Введите первый элемент массива - '))
d = int(input('Введите разность - '))
n = int(input('Введите количество элементов массива - '))
mas = []
for i in range(n):
    mas.extend([a1 + i * d])
print(f'элементы арифметической прогрессии - {mas}')
#asdasdasd
