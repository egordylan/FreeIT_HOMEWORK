'''* Создать большой массив из N = 1_000_000 элементов с отсортированными числами.
Массив генерируется случайным образом.
* Написать функцию, которая находит индекс элемента def find_idx(mass, target),
если элемент присутствует , иначе возвращается 'Number is not in array'.
* Померить сколько милисекунд ваша функция выполняется для какого-то значения
из массива с помощью 'import time'.'''

from random import randint
import time  # измеряем время, необходимое для выполнения скрипта этой штукой

start_time = time.time()
N = 1_000_000  # Количество элементов массива
array_random = [randint(1, N) for _ in range(N)]
print(N)
target = int(input('Ввести целое число в N: '))  # Число, индекс которого необходимо найти в массиве


def find_index(array_random, target):
    counter = 0
    for _ in range(N):
        a = sorted(array_random)
        if target in a[:target]:
            indx_target = a.index(target)
            return 'Index: ', indx_target
        else:
            counter += 1
            continue

    if counter == N:
            print('Number is not in array')
print(find_index(array_random, target))
print("--- %s seconds ---" % (time.time() - start_time))