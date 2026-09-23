class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        longest, current = 0, 0
        start = -1
        seen = {}
        for i in range(len(s)):
            last_seen = seen.get(s[i], -1)
            if last_seen > start:
                start = last_seen
            current = i - start
            seen[s[i]] = i  
            longest = max(longest, current)
        return longest

