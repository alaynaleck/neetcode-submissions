class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        prev = 0
        current = 1
        while current < len(prices):
            if prices[current] > prices[prev]:
                profit += prices[current] - prices[prev]
            prev = current
            current += 1
        return profit
            