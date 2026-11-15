import operator

class Solution:
    def calculate(self, s: str) -> int:
        PRECEDENCE = {"+": 1, "-": 1, "*": 2, "/": 2}
        OPERATIONS = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.floordiv,
        }
        
        def applyOperation():
            operation = stack.pop()
            right = nums.pop()
            left = nums.pop()
            nums.append(OPERATIONS[operation](left, right))

        # Cleanse the input of spaces
        s = "".join(s.split())

        element = ""
        nums, stack = [], []

        for char in s:
            # Build each number character by character
            if char not in OPERATIONS:
                element += char 
                continue

            # Truncate and append the finished number
            nums.append(int(element))
            element = ""

            # Apply higher order precendence using postfix
            while stack and PRECEDENCE[stack[-1]] >= PRECEDENCE[char]:
                applyOperation()
            stack.append(char)
    
        # Apply remaining operations
        nums.append(int(element))
        while stack:
            applyOperation()

        return nums[0]