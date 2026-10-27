class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixes = {0:1}
        currentSum = 0
        count = 0
        for num in nums:
            currentSum += num
            diff = currentSum - k
            count += prefixes.get(diff, 0)
            prefixes[currentSum] = prefixes.get(currentSum, 0) + 1
        return count