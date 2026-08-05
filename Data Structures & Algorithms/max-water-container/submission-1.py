class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area is defined by taking the min of the two containers 
        # and multiplying by the distance between the two indexes

        """
        take the current area with left and right pointer. then 
        """

        l, r = 0, len(heights) - 1
        max = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            
            if area > max:
                max = area
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max