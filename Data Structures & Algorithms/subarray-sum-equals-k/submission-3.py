class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # Map of prefix sums to the number of subarrays equal to that sum
        prefixes = {0: 1}

        # Track the resulting number of subarrays that are equal
        numEqualSubarrays = 0
        
        # The cumulative sum of the the numbers up to / including current
        runningSum = 0

        # For each number, calculate the running sum
        for num in nums:

            runningSum += num

            # Find the difference between the running sum and k
            diff = runningSum - k

            # If the difference exists within the map, add it to the total subarrays
            numEqualSubarrays += prefixes.get(diff, 0)

            # Update the runningSum count to one more, or add it 
            prefixes[runningSum] = prefixes.get(runningSum, 0) + 1
        
        return numEqualSubarrays