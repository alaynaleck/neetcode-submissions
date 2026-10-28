class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        total = 0
        prefixes = {0:1}
        for num in nums:
            total = (total + num) % k
            count += prefixes.get(total, 0)
            prefixes[total] = prefixes.get(total, 0) + 1
        return count

        