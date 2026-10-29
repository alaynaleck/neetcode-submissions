class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        maxDepth = 0
        for letter in s:
            if letter == "(":
                depth += 1
            elif letter == ")":
                depth -= 1
            maxDepth = max(depth, maxDepth)
        return maxDepth