class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def permute(current: str, numOpen: int, numClose: int):
            if numOpen == n and numClose == n:
                result.append(current)
                return
            if numOpen < n:
                permute(current + "(", numOpen + 1, numClose)
            if numClose < numOpen:
                permute(current + ")", numOpen, numClose + 1)
        permute("", 0, 0)
        return result

            

            
            