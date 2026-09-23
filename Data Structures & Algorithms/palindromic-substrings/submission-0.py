class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count = 0
        for i in range(len(s)): 
            start, end = i, i
            while start >= 0 and end < len(s) and s[start]==s[end]:
                count += 1
                start -= 1
                end += 1
        
        for i in range(len(s)-1):
            start, end = i, i+1
            while start >= 0 and end < len(s) and s[start]==s[end]:
                count += 1
                start -= 1
                end += 1
        return count