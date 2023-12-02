# 1. Найти все простые циклы в графе.

import networkx as nx

# Создаем граф
G = nx.DiGraph()  # Вы можете использовать nx.Graph() для ненаправленных графов
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (4, 1)])

# Находим все простые циклы в графе
cycles = nx.simple_cycles(G)

# Выводим количество циклов и сами циклы
num_cycles = 0
for cycle in cycles:
    num_cycles += 1
    print(f"Cycle {num_cycles}: {cycle}")

print(f"Cycles: {num_cycles}")


# 2. Проверить, является ли дерево симметричным.
#
# 3. Определить, является ли граф деревом.
#
# 4. Найти диаметр дерева.
#
# 5.* Написать свой класс для работы с графом.

# Класс для хранения узла бинарного дерева.
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# Функция для проверки того, являются ли поддеревья с корнем `X` и `Y` зеркальными друг другу
def isSymmetric(X, Y):
    # Базовый случай: если оба дерева пусты
    if X is None and Y is None:
        return True

    # возвращает true, если
    # 1. Оба дерева непусты, и
    # 2. Левое поддерево является зеркалом правого поддерева, и
    # 3. Правое поддерево является зеркалом левого поддерева
    return (X is not None and Y is not None) and \
        isSymmetric(X.left, Y.right) and \
        isSymmetric(X.right, Y.left)


# Функция для проверки того, имеет ли данное бинарное дерево симметричную структуру или нет.
def isSymmetricTree(root):
    # Базовый вариант
    if not root:
        return True

    # возвращает true, если левое и правое поддеревья зеркально отражают друг друга
    return isSymmetric(root.left, root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)

if isSymmetricTree(root):
    print('The binary tree is symmetric')
else:
    print('The binary tree is not symmetric')