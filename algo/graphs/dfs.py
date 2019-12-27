""" Depth-First Search """


# Connected Component
def dfs_connected_iterative(graph, start):
    visited, stack = set(), [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)

    return visited


def dfs_connected_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)

    for _next in graph[start] - visited:
        dfs_connected_recursive(graph, _next, visited)

    return visited


# Paths
def dfs_paths_iterative(graph, start, goal):
    stack = [(start, [start])]

    while stack:
        (vertex, path) = stack.pop()

        for _next in graph[vertex] - set(path):
            if _next == goal:
                yield path + [_next]
            else:
                stack.append((_next, path + [_next]))


def dfs_paths_recursive(graph, start, goal, path=None):
    if path is None:
        path = [start]

    if start == goal:
        yield path

    for _next in graph[start] - set(path):
        yield from dfs_paths_recursive(graph, _next, goal, path + [_next])


if __name__ == '__main__':
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

    print(dfs_connected_iterative(graph, 'A'))  # {'E', 'D', 'F', 'A', 'C', 'B'}
    print(dfs_connected_recursive(graph, 'C'))  # {'E', 'D', 'F', 'A', 'C', 'B'}

    print(list(dfs_paths_iterative(graph, 'A', 'F')))  # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]
    print(list(dfs_paths_recursive(graph, 'C', 'F')))  # [['C', 'F'], ['C', 'A', 'B', 'E', 'F']]
