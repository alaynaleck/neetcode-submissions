class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area is defined by taking the min of the two containers 
        # and multiplying by the distance between the two indexes

        max_area = 0
        left, right = 0, len(heights) - 1
        while right > left:
            area = min(heights[left], heights[right]) * (right - left)
            max_area = max(area, max_area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area