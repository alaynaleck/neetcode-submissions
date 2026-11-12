class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Start a pointer at the end of string
        right = len(s) - 1

        # Keep moving the pointer until the end of the last word
        # The end of the last word is the first non-space character
        while right >= 0 and s[right] == " ":
            right -= 1

        # Now, keep moving until the start of the last word
        # The start of the last word is the first non-space character
        left = right
        while left >= 0 and s[left] != " ":
            left -= 1

        return right - left


            