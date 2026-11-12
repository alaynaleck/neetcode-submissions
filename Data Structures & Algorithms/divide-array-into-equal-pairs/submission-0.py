class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        if len(nums) % 2 == 1:
            return False
        
        unmatched = set()
        for num in nums:
            if num not in unmatched:
                unmatched.add(num)
            else:
                unmatched.remove(num)
        
        return len(unmatched) == 0
