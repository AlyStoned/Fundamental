""" Breadth-First Search """

from collections import deque


# есть ли путь к узлу is_goal?
def bfs_iterative(root_nodes, graph, is_goal):
    checked = []
    dq = deque(root_nodes)

    while dq:
        curr_node = dq.popleft()
        print(curr_node, dq)

        if is_goal(curr_node):
            return curr_node

        checked.append(curr_node)

        for n in graph[curr_node]:
            if n not in checked and n not in dq:
                dq.append(n)


# Connected Component
def bfs_connected_iterative(graph, start):
    visited, queue = set(), [start]

    while queue:
        vertex = queue.pop(0)

        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)

    return visited


# Paths
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]

    while queue:
        (vertex, path) = queue.pop(0)

        for _next in graph[vertex] - set(path):
            if _next == goal:
                yield path + [_next]
            else:
                queue.append((_next, path + [_next]))


def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None


if __name__ == '__main__':
    """
            A
          /   \
         B     C
        / \  / |
       D   E   |
       |    \  /
       G      F
       
    """

    G = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'E', 'F'],
        'D': ['B', 'G'],
        'E': ['B', 'C', 'F'],
        'F': ['E'],
        'G': ['D'],
    }
    print(bfs_iterative(['A'], G, lambda n: n == 'G'))

    """
            A
          /   \
         B     C
        / \  / |
       D   E   |
            \  /
              F

    """
    graph = {
        'A': set(['B', 'C']),
        'B': set(['A', 'D', 'E']),
        'C': set(['A', 'F']),
        'D': set(['B']),
        'E': set(['B', 'F']),
        'F': set(['C', 'E'])
    }
    print(bfs_connected_iterative(graph, 'A'))  # {'B', 'C', 'A', 'F', 'D', 'E'}
    print(list(bfs_paths(graph, 'A', 'F')))  # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]
    print(shortest_path(graph, 'A', 'F'))  # ['A', 'C', 'F']
