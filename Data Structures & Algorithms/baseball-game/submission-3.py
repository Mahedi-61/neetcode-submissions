class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0

        for op in operations:
            if op == "+":
                temp = stack[-1] + stack[-2]
                res += temp 
                stack.append(temp)

            elif op == "D":
                temp = 2 * stack[-1]
                res += 2 * stack[-1]
                stack.append(temp)

            elif op == "C":
                res -= stack.pop()

            else:
                res += int(op)
                stack.append(int(op))

        return res