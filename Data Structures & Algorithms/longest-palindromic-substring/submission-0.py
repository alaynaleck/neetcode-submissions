class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def find_palindrome(start, end):
            if end >= len(s) or s[start]!= s[end]:
                return start, start
            while start in range(len(s)) and end in range(len(s)) and s[start]==s[end]:
                start -=1
                end += 1
            return start+1, end+1
        
        max_length, max_start, max_end = 0,0,0
        for i in range(len(s)):
            odd_start, odd_end = find_palindrome(i, i)
            even_start, even_end = find_palindrome(i, i+1)
            odd_length = odd_end - odd_start
            even_length = even_end - even_start

            if even_length > odd_length:
                length = even_length
                start, end = even_start, even_end
            else:
                length = odd_length
                start, end = odd_start, odd_end
            
            if length > max_length:
                max_length = length
                max_start = start
                max_end = end
        return s[max_start:max_end-1]