class Solution:
    def isValid(self, s: str) -> bool:
        br_dict = {"(":")", "{" : "}", "[" : "]"}

        stack = []
        for c in s:
            if c in [")", "}", "]"]:
                if len(stack) == 0: return False
                if c != br_dict[stack.pop()]:
                    return False 

            else:
                stack.append(c)

        return len(stack) == 0