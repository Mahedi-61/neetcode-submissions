class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(op, cl):
            if len(stack) == 2 * n:
                res.append("".join(stack))
                return

            if op < n:
                stack.append("(")
                op += 1
                backtrack(op, cl)
                stack.pop()
                op -= 1

            if cl < op:
                stack.append(")")
                cl += 1
                backtrack(op, cl)
                stack.pop()
                cl -= 1

        backtrack(0, 0)
        return res