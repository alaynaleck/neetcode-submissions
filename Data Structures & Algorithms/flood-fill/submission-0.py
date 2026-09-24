class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if image[sr][sc] == color:
            return image

        original_color, image[sr][sc] = image[sr][sc], color
        n, m = len(image), len(image[0])
        queue = deque([(sr, sc)])

        def color_pixel(row, col):
            if (row in range(n) and col in range(m)
                and image[row][col] == original_color):
                image[row][col] = color
                queue.append((row, col))
        
        while queue:
            row, col = queue.popleft()

            color_pixel(row-1, col)
            color_pixel(row+1, col)
            color_pixel(row, col-1)
            color_pixel(row, col+1)
        
        return image