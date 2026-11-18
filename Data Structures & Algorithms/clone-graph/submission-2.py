"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        clones = {} # key: original, val: clone
        queue = deque([node])
        clones[node] = Node(node.val)

        while queue:
            current = queue.popleft()
            for neighbor in current.neighbors:
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                clones[current].neighbors.append(clones[neighbor])
                
        return clones[node]

            

