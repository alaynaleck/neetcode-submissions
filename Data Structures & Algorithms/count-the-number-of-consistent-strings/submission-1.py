class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        letters = set(list(allowed))
        count = 0
        for word in words:
            valid = True
            for char in word:
                if char not in letters:
                    valid = False
                    continue
            count += 1 if valid else 0
        return count