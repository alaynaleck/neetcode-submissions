class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        counts = {}
        for num in arr:
            counts[num] = counts.get(num, 0) + 1

        greatestLucky = -1
        for num, count in counts.items():
            if num == count:
                greatestLucky = max(greatestLucky, count)
        
        return greatestLucky
            