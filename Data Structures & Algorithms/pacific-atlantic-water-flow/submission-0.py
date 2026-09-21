class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()
        pacific_queue, atlantic_queue = deque(), deque()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Pacific ocean cells (top and left edges)
        for row in range(len(heights)):
            pacific.add((row, 0))
            pacific_queue.append((row, 0))
        for col in range(len(heights[0])):
            pacific.add((0, col))
            pacific_queue.append((0, col))

        # Atlantic ocean cells (bottom and right edges)
        for row in range(len(heights)):
            atlantic.add((row, len(heights[0]) - 1))
            atlantic_queue.append((row, len(heights[0]) - 1))
        for col in range(len(heights[0])):
            atlantic.add((len(heights) - 1, col))
            atlantic_queue.append((len(heights) - 1, col))

        def bfs(queue, ocean):
            while queue:
                row, col = queue.popleft()
                height = heights[row][col]
                
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < len(heights) and 0 <= nc < len(heights[0])
                        and (nr, nc) not in ocean and heights[nr][nc] >= height):
                        ocean.add((nr, nc))
                        queue.append((nr, nc))

        bfs(pacific_queue, pacific)
        bfs(atlantic_queue, atlantic)

        return [list(cell) for cell in pacific & atlantic]