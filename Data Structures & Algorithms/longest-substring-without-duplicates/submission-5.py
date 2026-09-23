class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # p: start = -1, last_seen = -1, current = 0 - -1 = 1, p = 0
        # w: start = -1, last_seen = -1, current = 1 - -1 = 2, w = 1
        # w: start = -1, last_seen = 1, start = 1, current = 2 - 1, w = 2
        # 

        # we need to clear everything up to that last index
        # seen = set()
        # OH two pointer? 
        longest, current = 0, 0
        start = -1
        seen = {}
        for i in range(len(s)):
            last_seen = seen.get(s[i], -1)
            #print(f"char: {s[i]}, start: {start}, last_seen: {last_seen}")
            if last_seen > start:
                start = last_seen
            current = i - start
            seen[s[i]] = i  
            #print(f"char: {s[i]}, start: {start}, current: {current}")      
            longest = max(longest, current)
        return longest

