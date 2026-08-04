class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openBrackets = ['(', '{', '[']
        closeBrackets = {'}': '{', ')':'(', ']':'['}
        for char in s:
            if char in openBrackets:
                stack.append(char)
            elif char in closeBrackets:
                if not stack or stack.pop() != closeBrackets[char]:
                    return False
        
        return len(stack) == 0
