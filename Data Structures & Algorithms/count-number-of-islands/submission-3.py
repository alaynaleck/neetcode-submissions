class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        N = len(grid)
        M = len(grid[0])
        num_islands = 0

        def get_neighbors(row, col):
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            neighbors = []
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                if nr >= 0 and nr < N and nc >= 0 and nc < M:
                    neighbors.append((nr, nc))
            return neighbors

        def bfs(row, col):
            queue = deque([(row, col)])
            grid[row][col] = "0"
            while queue:
                r, c = queue.popleft()
                
                neighbors = get_neighbors(r, c)
                for nr, nc in neighbors:
                    if grid[nr][nc] == "1":
                        queue.append((nr, nc))
                        grid[nr][nc] = "0"

        for row in range(N):
            for col in range(M):
                if grid[row][col] == "1":
                    bfs(row, col)
                    num_islands += 1

        return num_islands
