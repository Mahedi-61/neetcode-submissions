class Solution:
    import math 
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in ["+", "-", "*", "/"]:
                b = stack.pop()
                a = stack.pop()

                if t == "+":
                    stack.append(a + b)

                elif t == "-":
                    stack.append(a - b)

                elif t == "*":
                    stack.append(a * b)

                elif t == "/":
                    val = a / b
                    if val > 0:
                        stack.append(math.floor(val))
                    else:
                        stack.append(math.ceil(val))
            else:
                stack.append(int(t))

        return stack[-1]