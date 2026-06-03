class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        b_dict = {")": "(", "}": "{", "]" : "["}

        for c in s:
            if c in ["(", "{", "["]:
                stack.append(c)
            
            else:
                if len(stack) != 0:
                    val = stack.pop()

                    if val != b_dict[c]:
                        return False 
                else:
                    return False

        return True if len(stack) == 0 else False  