"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloned = {} # key: original, val: cloned
        def dfs(node):
            if node in cloned:
                return cloned[node]

            cloned[node] = Node(node.val)
            for neighbor in node.neighbors:
                cloned[node].neighbors.append(dfs(neighbor))
                
            return cloned[node]
        
        return dfs(node) if node else None

            

