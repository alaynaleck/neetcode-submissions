class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # create a hashmap of freqs
        # create an array (size length fo the list)
        # for each element in hashmap, add to the bucket
        result = []

        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        # Sort them into the most frequently occurring elements
        freqs = [[] for _ in range(len(nums))]
        for num, count in counts.items():
            freqs[count-1].append(num)

        i = len(nums)-1
        while len(result) < k and i >= 0:
            elements = freqs[i]
            for element in elements:
                result.append(element)
            i -= 1
        
        return result

        
