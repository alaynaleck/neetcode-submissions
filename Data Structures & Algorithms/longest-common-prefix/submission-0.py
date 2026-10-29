class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = float("inf")
        prefix = ""
        for word in strs:
            shortest = min(shortest, len(word))

        for i in range(shortest):
            letter = strs[0][i]
            for word in strs:
                if word[i] != letter:
                    return prefix
            prefix = prefix + letter
        return prefix