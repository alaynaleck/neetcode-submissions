class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastSeen = {} # letter: most recent index
        start = end = longest = 0

        while end < len(s):
            char = s[end]
            if char in lastSeen and lastSeen[char] > start:
                start = lastSeen[char]
            end += 1
            lastSeen[char] = end
            longest = max(longest, end-start)
        return longest
