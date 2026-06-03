class Solution:
    def isValid(self, s: str) -> bool:
        dt_parent = {")":"(", "}":"{", "]":"["}
        stack = []

        for c in s:
            if c in [")", "}", "]"]:
                if not stack or dt_parent[c] != stack.pop():
                    return False
            else:
                stack.append(c)

        return True if not stack else False