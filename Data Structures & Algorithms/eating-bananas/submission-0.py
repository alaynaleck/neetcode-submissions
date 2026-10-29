class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = math.ceil(sum(piles) / h)
        right = max(piles)
        largest = right

        while left <= right:
            k = (right - left) // 2 + left
            time = 0
            for pile in piles:
                time += math.ceil(pile/k)
            if time <= h:
                largest = k
                right = k - 1
            else:
                left = k + 1
        return largest
                    

