class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        left, right = max(weights), sum(weights)
        minCapacity = right

        def works(capacity, days):
            daysUsed = 1
            currentWeight = 0
            
            for weight in weights:

                # Start a new day using the package
                if currentWeight + weight > capacity:
                    daysUsed += 1
                    currentWeight = 0
                currentWeight += weight

            return daysUsed <= days

        while left <= right:
            capacity = (right + left) // 2
            if works(capacity, days):
                minCapacity = min(minCapacity, capacity)
                right = capacity - 1
            else:
                left = capacity + 1
        
        return minCapacity
