# 1. Найти все простые циклы в графе.

import networkx as nx
#
# # Создаем граф
# G = nx.DiGraph()
# G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (4, 1)])

# Находим все простые циклы в графе
# cycles = nx.simple_cycles(G)

# Выводим количество циклов и сами циклы
# num_cycles = 0
# for cycle in cycles:
#     num_cycles += 1
#     print(f"Cycle {num_cycles}: {cycle}")
#
# print(f"Cycles: {num_cycles}")


# 2. Проверить, является ли дерево симметричным.

# def is_symmetric(G):
#     edges = G.edges()
#
#     for u, v in edges:
#         if (v, u) not in edges:
#             return False
#
#     return True
#
#
# G = nx.Graph()
# G.add_nodes_from([1, 2, 3, 4])
# G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4)])
#
# print(is_symmetric(G))


# 3. Определить, является ли граф деревом.

# import networkx as nx
#
#
# def has_cycle(G):
#     visited = set()
#     in_stack = set()
#
#     def dfs(node):
#         visited.add(node)
#         in_stack.add(node)
#
#         for neighbor in G.neighbors(node):
#             if neighbor in visited and neighbor not in in_stack:
#                 return True
#
#             if neighbor not in visited:
#                 if dfs(neighbor):
#                     return True
#
#         in_stack.remove(node)
#         return False
#
#     for node in G.nodes():
#         if node not in visited:
#             if dfs(node):
#                 return True
#
#     return False
#
#
# G = nx.Graph()
# G.add_nodes_from([1, 2, 3, 4])
# G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4)])
#
# print(has_cycle(G))


# 4. Найти диаметр дерева.

# import networkx as nx
#
#
# def diameter(G):
#     """
#   Находит диаметр дерева.
#
#   Args:
#     G: Граф, представляющий дерево.
#
#   Returns:
#     Число, равное диаметру дерева.
#   """
#
#     if not nx.is_tree(G):
#         raise ValueError("Граф не является деревом")
#
#     # Находим самую длинную цепочку в дереве.
#
#     chain = nx.shortest_path(G, source=None, target=None, weight=None)
#
#     return len(chain) - 1
#
# G = nx.Graph()
# G.add_edge(1, 2)
# G.add_edge(2, 3)
# G.add_edge(3, 4)
# G.add_edge(4, 5)
# G.add_edge(5, 6)
# G.add_edge(6, 7)
#
# print(diameter(G))

# 5.* Написать свой класс для работы с графом.

import networkx as nx


class Tree:
    """
    Класс для работы с деревом.

    Args:
        G: Граф, представляющий дерево.
    """

    def __init__(self, G):
        self._G = G
        self._root = find_root(G)

    @property
    def root(self):
        """
        Возвращает корень дерева.

        Returns:
            Вершина, являющаяся корнем дерева.
        """

        return self._root

    def is_symmetric(self):
        """
        Проверяет, является ли дерево симметричным.

        Returns:
            True, если дерево симметрично, False в противном случае.
        """

        edges = self._G.edges()

        for u, v in edges:
            if (v, u) not in edges:
                return False

        return True

    def has_cycle(self):
        """
        Определяет, является ли граф деревом.

        Returns:
            True, если граф является деревом, False в противном случае.
        """

        visited = set()
        in_stack = set()

        def dfs(node):
            visited.add(node)
            in_stack.add(node)

            for neighbor in self._G.neighbors(node):
                if neighbor in visited and neighbor not in in_stack:
                    return True

                if neighbor not in visited:
                    if dfs(neighbor):
                        return True

            in_stack.remove(node)
            return False

        for node in self._G.nodes():
            if node not in visited:
                if dfs(node):
                    return True

        return False

    def diameter(self):
        """
        Находит диаметр дерева.

        Returns:
            Число, равное диаметру дерева.
        """

        if not self.is_tree():
            raise ValueError("Граф не является деревом")

        # Находим самую длинную цепочку в дереве.

        chain = nx.shortest_path(self._G, source=None, target=None, weight=None)

        return len(chain) - 1

