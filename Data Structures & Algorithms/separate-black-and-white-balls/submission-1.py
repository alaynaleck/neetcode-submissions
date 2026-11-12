class Solution:
    def minimumSteps(self, s: str) -> int:
        BLACK = "0"
        targetPosition = 0
        minimumSwaps = 0
        for actualPosition in range(len(s)):
            if s[actualPosition] == BLACK:
                minimumSwaps += actualPosition - targetPosition
                targetPosition += 1
        return minimumSwaps
