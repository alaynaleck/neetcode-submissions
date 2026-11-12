class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        if previous < current, previous = current
        """

        if len(prices) == 1:
            return 0

        profit = 0
        prev = 0
        current = 1
        while current < len(prices):
            if prices[current] > prices[prev]:
                profit += prices[current] - prices[prev]
            prev = current
            current += 1
        return profit
            