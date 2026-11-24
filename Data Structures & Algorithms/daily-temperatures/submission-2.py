class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0 for i in range(len(temperatures))]
        stack = [] # decreasing stack

        for i in range(len(temperatures)):
            temp = temperatures[i]
            while stack and temp > stack[-1][0]:
                _, date = stack.pop()
                result[date] = i - date
            stack.append([temp, i])

        return result

