class Solution:
    def minimumSteps(self, s: str) -> int:
        targetPosition = 0
        minimumSwaps = 0
        for actualPosition in range(len(s)):
            if s[actualPosition] == "0":
                minimumSwaps += actualPosition - targetPosition
                targetPosition += 1
        return minimumSwaps
