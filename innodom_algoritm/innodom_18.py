# Задача 1 Реализовать алгоритм сортировки слиянием. Примечание: Он заключается в разделении исходного массива на две
# равные половины, сортировке каждой из половин и последующем их слиянии в отсортированный массив. Важно: запрещено
# использовать стандартные функции сортировки в python.

my_array = [2, 5, 64, 348796, 346, 24, 6, 6, 37, 57, 45, 62, 5, 253, 6, 468, 69, 69, 0, 795, 2682, 3, 9, 9, 0, 7, 57,
            6768, 8, 4675]


def merge_sort(my_array):
    if len(my_array) <= 1:
        return my_array
    else:
        pivot = my_array[len(my_array) // 2]
        left = [i for i in my_array if i < pivot]
        middle = [i for i in my_array if i == pivot]
        right = [i for i in my_array if i > pivot]
    return merge_sort(left) + middle + merge_sort(right)


print(merge_sort(my_array))

# Задача 2 Дан упорядоченный по возрастанию массив с числами, требуется сгенерировать все его перестановки. Перестановка
# n объектов/элементов — это способ их последовательного расположения с учётом порядка. Например: abc, bca и cab — это
# разные перестановки трёх букв. Решите задачу итерационно и рекурсивно. Опишите, какой подход лучше и почему.

my_array = [1, 2, 3, 4]


def permutations(my_array, result=''):
    my_array = ''.join([str(i) for i in my_array])

    if len(my_array) == 0:
        print(result)

    for i in range(len(my_array)):
        new_array = result + my_array[i]
        new_result = my_array[0:i] + my_array[i + 1:]
        permutations(new_result, new_array)


permutations(my_array)


# Итеративная функция для генерации всех перестановок строки в Python
def permutations(my_array):
    my_array = ''.join([str(i) for i in my_array])
    # Базовый вариант
    if not my_array:
        return []

    # создать список для хранения (частичных) перестановок
    partial = []

    # инициализирует список первым символом строки
    partial.append(my_array[0])

    # делать для каждого символа указанной строки
    for i in range(1, len(my_array)):

        # рассматривает ранее построенные частичные перестановки одну за другой

        # итерация назад
        for j in reversed(range(len(partial))):

            # удалить текущую частичную перестановку из списка
            curr = partial.pop(j)

            # Вставить следующий символ указанной строки во все
            # возможных позиций текущей частичной перестановки.
            # Затем вставьте каждую из этих вновь созданных строк в список.

            for k in range(len(curr) + 1):
                partial.append(curr[:k] + my_array[i] + curr[k:])

    print(partial, end='')


permutations(my_array)

# способ лучше: никакой
# все одинаково не понятно)
