class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # how can we check if they're unique? 
        unique = set()
        result = []
        nums.sort()

        for i in range(len(nums)):
            current_sum = -nums[i]
            left, right = i+1, len(nums)-1
            
            # Traverse with two pointers where -current = left + right
            while left < right:
                val = nums[left] + nums[right]
                if val == current_sum:
                    unique.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif val > current_sum:
                    right -= 1
                else:
                    left += 1
        
        # Only use unique values
        for i, j, k in unique:
            result.append([i, j, k])

        return result

