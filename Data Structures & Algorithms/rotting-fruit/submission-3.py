class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh_fruit = 0
        minutes = 0
        
        # Add each rotting fruit to a queue for BFS
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row, col, minutes))
                elif grid[row][col] == 1:
                    fresh_fruit += 1

        def add_fruit(row, col, minutes):
            nonlocal fresh_fruit
            if (row >= 0 and row < len(grid) 
                and col >= 0 and col < len(grid[0])
                and grid[row][col] == 1):
                queue.append((row, col, minutes))
                grid[row][col] = 2
                fresh_fruit -= 1
        
        # Multi-way bfs to track how much time for each fruit
        while queue:
            row, col, minutes = queue.popleft()
            
            add_fruit(row - 1, col, minutes + 1)
            add_fruit(row + 1, col, minutes + 1)
            add_fruit(row, col - 1, minutes + 1)
            add_fruit(row, col + 1, minutes + 1)

        # If a fresh fruit is found, then the state is unachievable
        if fresh_fruit > 0:
            return -1

        return minutes


    