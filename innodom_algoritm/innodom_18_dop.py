# 1. Найти все простые циклы в графе.

import networkx as nx

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

# class MyGraph:
#
#     def __init__(self, nodes=None, edges=None, directed=False):
#         self.graph = nx.Graph(directed)
#
#         if nodes is not None:
#             for node in nodes:
#                 self.graph.add_node(node)
#
#         if edges is not None:
#             for edge in edges:
#                 self.graph.add_edge(*edge)
#
#     def add_node(self, node):
#         self.graph.add_node(node)
#
#     def add_edge(self, node1, node2, weight=None):
#         self.graph.add_edge(node1, node2, weight)
#
#     def get_nodes(self):
#         return self.graph.nodes()
#
#     def get_edges(self):
#         return self.graph.edges()
#
#     def get_node_neighbors(self, node):
#         return self.graph.neighbors(node)
#
#     def get_edge_weight(self, node1, node2):
#         return self.graph.get_edge_data(node1, node2)['weight']
#
#     def set_edge_weight(self, node1, node2, weight):
#         self.graph.edges[node1, node2]['weight'] = weight
#
#     def remove_node(self, node):
#         self.graph.remove_node(node)
#
#     def remove_edge(self, node1, node2):
#         self.graph.remove_edge(node1, node2)
#
#     def __repr__(self):
#         return str(self.graph)
#
# nodes = ["A", "B", "C"]
# edges = [("A", "B", 10), ("B", "C", 20)]
#
# graph = MyGraph(nodes, edges)
#
# print(graph.get_nodes())
# # ['A', 'B', 'C']
#
# print(graph.get_edges())
# # [('A', 'B', {'weight': 10}), ('B', 'C', {'weight': 20})]
