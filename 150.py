class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def isInt(s):
            try:
                int(s)
                return True
            except:
                return False

        stack = []

        for i in tokens:
            if isInt(i):
                stack.append(i)

            else:
                b = int(stack.pop())
                a = int(stack.pop())

                if i == "+":
                    c = a + b
                elif i == "-":
                    c = a - b
                elif i == "*":
                    c = a * b
                elif i == "/":
                    c = int(a / b)

                stack.append(str(c))

        return stack[-1]
