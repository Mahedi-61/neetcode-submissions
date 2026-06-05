class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0
        for op in operations:
            if op == "+":
                num = stack[-2] + stack[-1]
                res += num
                stack.append(num)

            elif op == "C":
                res -= stack.pop()

            elif op == "D":
                num = stack[-1] * 2
                res += num
                stack.append(num)

            else:
                num = int(op)
                res += num
                stack.append(num)

        return res