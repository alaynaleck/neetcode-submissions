class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []
        def createParenthesis(numOpen, numClose):
            if numOpen == numClose == n:
                result.append("".join(stack))
            if numOpen < n:
                stack.append("(")
                createParenthesis(numOpen + 1, numClose)
                stack.pop()
            if numClose < numOpen:
                stack.append(")")
                createParenthesis(numOpen, numClose+1)
                stack.pop()
        createParenthesis(0, 0)
        return result

            

            
            