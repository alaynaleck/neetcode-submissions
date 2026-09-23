class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        for letter in s:
            counts[letter] = counts.get(letter, 0) + 1
        for letter in t:
            if letter not in counts:
                return False
            counts[letter] = counts[letter] - 1
        for letter in counts:
            if counts[letter] != 0:
                return False
        return True