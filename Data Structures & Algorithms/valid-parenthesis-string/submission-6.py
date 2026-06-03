class Solution:
    def checkValidString(self, s: str) -> bool:
        star_stack = []
        op_par_stack = []

        for i, c in enumerate(s):
            if c == "*":
                star_stack.append(i)
            elif c == "(":
                op_par_stack.append(i)
            else:
                if op_par_stack:
                    op_par_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False

        if len(star_stack) >= len(op_par_stack):
            while star_stack and op_par_stack:
                if op_par_stack[-1] < star_stack[-1]:
                    star_stack.pop()
                    op_par_stack.pop()
                else:
                    star_stack.pop()

            if op_par_stack:
                return False
        else:
           return False
        return True
