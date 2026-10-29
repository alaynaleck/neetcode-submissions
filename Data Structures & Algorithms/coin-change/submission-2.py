class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        amounts = {}

        def createChange(amount):
            if amount == 0:
                return 0

            if amount in amounts:
                return amounts[amount]
            
            minCount = float("inf")
            for coin in coins:
                if amount - coin >= 0:
                    count = 1 + createChange(amount - coin)
                    minCount = min(count, minCount)

            amounts[amount] = minCount
            return minCount
        
        minCoins = createChange(amount)
        return -1 if minCoins == float("inf") else minCoins
            