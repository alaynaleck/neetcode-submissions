class Solution:
    def countBits(self, n: int) -> List[int]:
        oneBits = [0] * (n+1)
        for i in range(n+1):
            oneBits[i] = oneBits[i >> 1] + (i & 1)
        return oneBits