class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Understand: given an array of numbers, return the k (ranked) most frequent elements
        - k = 1 means find the mode
        - k = 2 means find the top two most frequent numbers

        Input: 
        - No nums: return empty array COVERED
        - What happens if k < size(nums) or cardinality(nums) COVERED


        Match: 
        Hashmap: we can create key value pairs to find the frequency of appearance in each number

        """

        freqs = {}
        buckets = [[] for i in range(len(nums) + 1)]
        result = []
        
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1
        
        for num, count in freqs.items():
            buckets[count].append(num)

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

        return result
        
