class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Iterate through each element
        # Mark seen as 0
        # If unseen, perform dfs, counting 1 per item in the stack
        # While appending neighbors, mark as 0
        N, M = len(grid), len(grid[0])
        max_area = 0

        def dfs(start_row, start_col):
            grid[start_row][start_col] = 0
            stack = [(start_row, start_col)]
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            area = 0
            while stack:
                row, col = stack.pop()
                area += 1
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr >= 0 and nr < N and nc >= 0 and nc < M and grid[nr][nc] == 1:
                        stack.append((nr, nc))
                        grid[nr][nc] = 0
            return area

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    area = dfs(row, col)
                    max_area = max(area, max_area)
        return max_area

        
                