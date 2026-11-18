class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        num_islands = 0
        
        def dfs(row, col):
            if row not in range(len(grid)) or col not in range(len(grid[0])):
                return
            if grid[row][col] == "X" or grid[row][col] == "0":
                return
            grid[row][col] = "X"
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
            
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    dfs(row, col)
                    num_islands += 1

        return num_islands
