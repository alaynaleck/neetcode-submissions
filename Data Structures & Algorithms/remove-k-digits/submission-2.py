class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k > 0 and stack and int(stack[-1]) > int(digit):
                stack.pop()
                k -= 1
            stack.append(digit)
        stack = stack[:len(stack)-k]
        result = ""
        return "".join(stack).lstrip("0") or "0"