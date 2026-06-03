class Solution:
    def checkValidString(self, s: str) -> bool:
        left_stack = []
        start_stack = []

        for i, c in enumerate(s):
            if c == ")":
                if left_stack:
                    left_stack.pop()

                elif start_stack:
                    start_stack.pop()

                else:
                    return False

            elif c == "(":
                left_stack.append(i)

            else:
                start_stack.append(i)

        while left_stack and start_stack:
            if start_stack[-1] > left_stack[-1]:
                left_stack.pop()

            start_stack.pop()
        
        return len(left_stack) == 0