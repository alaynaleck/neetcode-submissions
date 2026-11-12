class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        bits = 0
        for char in allowed:
            bit = 1 << (ord(char) - ord('a'))
            bits |= bit

        count = len(words)
        for word in words:
            valid = True
            for char in word:
                bit = 1 << (ord(char) - ord('a'))
                if bit & bits == 0:
                    count -= 1
                    break
        return count