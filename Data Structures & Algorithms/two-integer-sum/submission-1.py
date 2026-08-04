class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            left = target - num
            if left in hashmap:
                return [hashmap[left], i]
            
            hashmap[num] = i
        
        return [0, 0]
