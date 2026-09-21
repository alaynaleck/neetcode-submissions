class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # every time you reach a zero, bfs
        # change the inf to the current level 
        # (min the current level and its existing value)
        # Are treasure chests traversable? 
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        N, M = len(grid), len(grid[0])
        distance = 0
        queue = deque()
        visited = set()
        
        # Traverse each grid cell one by one
        for row in range(N):
            for col in range(M):
                if grid[row][col] == 0:
                    queue.append((row, col, distance))
                    visited.add((row, col))

        # bfs from each treasure chest
        while queue:
            row, col, current_dist = queue.popleft()
            # If the current treasure chest is closer, update
            grid[row][col] = current_dist
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                # Skip invalid indices or treasure chests
                if (nr < 0 or nr >= N 
                    or nc < 0 or nc >= M 
                    or (nr, nc) in visited
                    or grid[nr][nc] == 0 or grid[nr][nc] == -1):
                    continue
                queue.append((nr, nc, current_dist + 1))
                visited.add((nr, nc))
        return 

