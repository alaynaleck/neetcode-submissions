class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        N, M = len(grid), len(grid[0])
        max_area = 0

        # Perform DFS to find the size of an island given a starting point
        def dfs(start_row, start_col):
            grid[start_row][start_col] = 0
            stack = [(start_row, start_col)]
            area = 0

            while stack:
                row, col = stack.pop()
                area += 1

                # Append neighbors
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    
                    # Indentify if neighbors are in bounds and land
                    if (nr >= 0 and nr < N and nc >= 0 
                        and nc < M and grid[nr][nc] == 1):
                        
                        stack.append((nr, nc))
                        grid[nr][nc] = 0 # Mark neighbors as seen
            return area

        # Visit each item on the board
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    area = dfs(row, col)
                    max_area = max(area, max_area)
        return max_area

        
                