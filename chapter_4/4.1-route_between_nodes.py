from __future__ import annotations

from collections import deque


class Node:
    def __init__(self, value: int = 0):
        self.value = value
        self.neighbours: set[Node] = set()
    
    def add_neighbour(self, neighbours: list[Node]) -> None:
        for neighbour in neighbours:
            if neighbour not in self.neighbours:
                self.neighbours.add(neighbour)


def route_between_nodes_dfs(source: Node, dest: Node)->bool:
    """
    using DFS
    """
    
    def dfs(node: Node)->bool:
        if not node:
            return False
        
        if node == dest:
            return True
        
        for neighbour in node.neighbours:
            if dfs(neighbour):
                return True
        
        return False
    
    return dfs(source)
    
def route_between_nodes(source: Node, dest: Node)-> bool:
    """
    using BFS
    """
    visited = set()
    queue = deque()
    queue.append(source)
    while queue:
        cur_node = queue.popleft()
        if cur_node==dest:
            return True
        visited.add(cur_node)
        for neighbour in cur_node.neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
    return False
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.add_neighbour([b,c])
# b.add_neighbour([d])
# c.add_neighbour([d])

print(route_between_nodes(a, d))
print(route_between_nodes_dfs(a, d))

