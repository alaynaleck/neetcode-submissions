class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        freshFruit = 0
        minutes = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    freshFruit += 1
                elif grid[row][col] == 2:
                    queue.append((row, col, minutes))

        def addFruit(row, col, minutes):
            nonlocal freshFruit
            if row not in range(len(grid)) or col not in range(len(grid[0])) or grid[row][col] != 1:
                return
            queue.append((row, col, minutes))
            grid[row][col] = 2
            freshFruit -= 1
            
        while queue:
            row, col, minutes = queue.popleft()

            addFruit(row + 1, col, minutes + 1)
            addFruit(row - 1, col, minutes + 1)
            addFruit(row, col + 1, minutes + 1)
            addFruit(row, col - 1, minutes + 1)

        return minutes if freshFruit == 0 else -1
        


            

        

    