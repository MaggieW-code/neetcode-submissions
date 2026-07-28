class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }

        stack = []
        for i in tokens:
            if i in operations:
                num1 = stack.pop()
                num2 = stack.pop()
                tempnum = operations[i](int(num2), int(num1))
                stack.append(tempnum)
            else:
                stack.append(i)
        return (int(stack.pop()))
            