# 1. Найти все простые циклы в графе.

import networkx as nx

# Создаем граф
G = nx.DiGraph()
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

def is_symmetric(G):
    edges = G.edges()

    for u, v in edges:
        if (v, u) not in edges:
            return False

    return True


G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4)])

print(is_symmetric(G))


# 3. Определить, является ли граф деревом.

import networkx as nx


def has_cycle(G):
    visited = set()
    in_stack = set()

    def dfs(node):
        visited.add(node)
        in_stack.add(node)

        for neighbor in G.neighbors(node):
            if neighbor in visited and neighbor not in in_stack:
                return True

            if neighbor not in visited:
                if dfs(neighbor):
                    return True

        in_stack.remove(node)
        return False

    for node in G.nodes():
        if node not in visited:
            if dfs(node):
                return True

    return False


G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4)])

print(has_cycle(G))


# 4. Найти диаметр дерева.

import networkx as nx


def diameter(G):
    """
  Находит диаметр дерева.

  Args:
    G: Граф, представляющий дерево.

  Returns:
    Число, равное диаметру дерева.
  """

    if not nx.is_tree(G):
        raise ValueError("Граф не является деревом")

    # Находим самую длинную цепочку в дереве.

    chain = nx.shortest_path(G, source=None, target=None, weight=None)

    return len(chain) - 1

G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 5)
G.add_edge(5, 6)
G.add_edge(6, 7)

print(diameter(G))

# 5.* Написать свой класс для работы с графом.

class Graph:
    """
    Класс для работы с графом.

    Attributes:
        G: Объект класса `nx.Graph`, представляющий граф.
    """

    def __init__(self):
        self.G = nx.Graph()

    def add_node(self, node):
        """
        Добавляет узел в граф.

        Args:
            node: Номер узла.
        """
        self.G.add_node(node)

    def add_edge(self, u, v):
        """
        Добавляет ребро в граф.

        Args:
            u: Номер узла u.
            v: Номер узла v.
        """
        self.G.add_edge(u, v)

    def diameter(self):
        """
        Находит диаметр графа.

        Returns:
            Число, равное диаметру графа.
        """
        if not nx.is_tree(self.G):
            print("A graph is not a tree")
        else:
            print("A graph is a tree")
        # Находим самую длинную цепочку в дереве.

        chain = nx.shortest_path(self.G, source=None, target=None, weight=None)

        return len(chain) - 1

    def has_cycle(self):
        """
        Проверяет наличие цикла в графе.

        Returns:
            True, если граф содержит цикл, False - иначе.
        """
        visited = set()
        in_stack = set()

        def dfs(node):
            visited.add(node)
            in_stack.add(node)

            for neighbor in self.G.neighbors(node):
                if neighbor in visited and neighbor not in in_stack:
                    return True

                if neighbor not in visited:
                    if dfs(neighbor):
                        return True

            in_stack.remove(node)
            return False

        for node in self.G.nodes():
            if node not in visited:
                if dfs(node):
                    return True

        return False

    def is_symmetric(self):
        """
        Проверяет симметрию графа.

        Returns:
            True, если граф является симметричным, False - иначе.
        """
        edges = self.G.edges()

        for u, v in edges:
            if (v, u) not in edges:
                return False

        return True

import networkx as nx

# Создаем граф
graph = Graph()

# Добавляем узлы
graph.add_node(1)
graph.add_node(2)
graph.add_node(3)
graph.add_node(4)

# Добавляем ребра
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 5)

# Находим диаметр графа
diameter = graph.diameter()
print("Find the diameter of the graph:", diameter)

# Проверяем наличие цикла в графе
has_cycle = graph.has_cycle()
print("Check if there is a cycle in the graph:", has_cycle)

# Проверяем симметрию графа
is_symmetric = graph.is_symmetric()
print("Check the symmetry of the graph:", is_symmetric)
