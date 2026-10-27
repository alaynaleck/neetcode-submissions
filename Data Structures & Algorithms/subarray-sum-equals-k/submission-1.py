class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Inputs:
        - array of positive and negative numbers
        - target sum (positive or negative)
        - increasing the size of the arry is not gauranteed to increase the sum of the array
        - decreasing the size of the array is not gauranteed ot decrease the sum of the array
        Output:
        - count of all separate subsets of sums that equal k, order matters for elements so they are considered distinct, as well as later seen [-1, 1] and [-1, 1]
        
        Match: 
        
        Thinking:
        - starting at a given element, there is only a subset of ways that this could match, we would never want to go backwards. 
        """
        prefixes = {0:1}
        currentSum = 0
        count = 0
        for num in nums:
            currentSum += num
            diff = currentSum - k
            count += prefixes.get(diff, 0)
            prefixes[currentSum] = prefixes.get(currentSum, 0) + 1
        return count