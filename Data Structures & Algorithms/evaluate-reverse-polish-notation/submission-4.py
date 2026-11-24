class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        def applyOperation(operation):
            b = stack.pop()
            a = stack.pop()
            if operation == "+":
                stack.append(a + b)
            elif operation == "-":
                stack.append(a - b)
            elif operation == "*":
                stack.append(a * b)
            elif operation == "/":
                stack.append(int(float(a)/b))

        for token in tokens:
            if token in ["+", "-", "/", "*"]:
                applyOperation(token)
            else:
                stack.append(int(token))
        return stack[-1]
            
