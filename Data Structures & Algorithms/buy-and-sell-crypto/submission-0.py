class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Understand: 
        Input: array of ints
        - Length 0: 0
        - Length 1: 0
        - i < j and array[i] < array[j]
        Return: 
        Int where i < j and array[j] - array[i] = max

        Match: 
        Sliding window

        Plan: 
        1. If len prices <= 1 return 0
        2. initialize i = 0 and j = 1
        3. if arr[i] < arr[j], : profit = arr[j] - arr[i] 
        4. if arr[i] >= arr[j], i++ j++ 
        5. 
        """
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                max_profit = max(max_profit, prices[j]-prices[i])
        return max_profit

