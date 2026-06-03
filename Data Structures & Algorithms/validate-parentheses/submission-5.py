class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        br_dict = {"(" : ")", "{" : "}", "[" : "]"}

        for c in s:
            if c in [')', '}', ']']:
                if not stack:
                    return False 
                    
                if c != br_dict[stack.pop()]:
                    return False 
            else:
                stack.append(c)

        return len(stack) == 0