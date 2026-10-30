class Solution:
    def reorganizeString(self, s: str) -> str:
        freqs = {}
        heap = []
        wait = None
        result = ""
        for letter in s:
            freqs[letter] = freqs.get(letter, 0) + 1
        
        for letter, count in freqs.items():
            heapq.heappush(heap, (-count, letter))

        while heap or wait:

            if wait and not heap:
                return ""

            count, letter = heapq.heappop(heap)
            result = result + letter
            
            if wait:
                heapq.heappush(heap, wait)
                wait = None
            
            if count + 1 < 0:
                wait = (count + 1, letter)    

        return result
