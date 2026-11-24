class Solution:
    def climbStairs(self, n: int) -> int:
        """
        1 stair: 1 way
        2 stairs: 2 ways, 2 steps and 2 one steps
        3 stairs: 3 ways, 2 steps + 1, 1 step + 2, 1, 1, 1
        4 steps: 1 + 1 + 1 + 1, 2 + 2, 2 + 1 + 1, 1 + 2 + 1, 1 + 1 + 2
        """

        if n <= 2:
            return n
        
        steps = [0 for i in range(n+1)]
        steps[1] = 1
        steps[2] = 2

        for i in range(3, n+1):
            steps[i] = steps[i-1] + steps[i-2]
        return steps[-1]