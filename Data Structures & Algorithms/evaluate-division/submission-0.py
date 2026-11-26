class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        nodes = {}
        for i in range(len(equations)):
            a, b = equations[i]
            value = values[i]
            nodes[a] = nodes.get(a, []) + [(b, value)]
            nodes[b] = nodes.get(b, []) + [(a, 1 / value)]
        
        def dfs(node, target, seen):
            
            if node not in nodes or target not in nodes:
                return -1
            if node == target:
                return 1
            
            seen.add(node)
            for neighbor, weight in nodes.get(node, []):
                if neighbor not in seen:
                    result = dfs(neighbor, target, seen)
                    if result != -1:
                        return weight * result
            return -1
        return [dfs(q[0], q[1], set()) for q in queries]
            



