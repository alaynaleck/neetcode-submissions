class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Understand:
        - Return the number of days before a warmer temp appears
        - Nothing larger, return 0
        - The last value will always be zero (there's nothing else to compare to)
        Happy Case:
        - [30,80,30,36] -> 1,0,1,0
        Edge Case:
        - Strictly Increasing: [30,31,32] -> [1,1,0]
        - Strictly Decreasing: [0,0,0]
        - Same values: [30,30,30] -> [0,0,0]
        Match:
        - Monotonic Stack: since we're looking at increases and decreases in temperature, to me this looks like a situation where I might want to track only increasing or decreasing values and pop the rest
        - Monotonic Decreasing: once we've seen a greater number, we stop the count and we don't necessarily care about anything less than it
        Plan:
        - Initialize a stack. The top will always be the largest number and the bottom will always be the greatest
        - For each number in temperatures, we are going to compare it to the top of the stack if it exists:
        - if less than equal to the top of the stack, we are going to add it 
        - while it's greater than the top of the stack, we are going to pop the element in the stack. then, we are going to update that index to the difference between its index and that index, finally, we're going to push it to the stack
        """

        result = [0 for i in range(len(temperatures))]
        stack = [] # decreasing stack

        for i in range(len(temperatures)):
            temp = temperatures[i]
            while stack and temp > stack[-1][0]:
                _, date = stack.pop()
                result[date] = i - date
            stack.append([temp, i])

        return result

