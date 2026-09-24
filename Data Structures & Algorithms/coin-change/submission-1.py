class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        amounts = {}
        
        def makeChange(amount):
            if amount == 0:
                return 0
            if amount in amounts:
                return amounts[amount]

            min_coins = float("inf")
            for coin in coins:
                if amount - coin >= 0:
                    min_coins = min(min_coins, 1 + makeChange(amount - coin))
            
            amounts[amount] = min_coins
            return min_coins
        
        min_coins = makeChange(amount)
        return -1 if min_coins >= float("inf") else min_coins
             