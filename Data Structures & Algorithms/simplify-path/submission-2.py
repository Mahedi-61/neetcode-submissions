class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")

        for p in path:
            if not stack and p == "..":
                continue
            elif "/" in p or p == "." or p == "":
                continue
            elif p == "..":
                stack.pop()
            else:
                stack.append(p)

        return "/" + "/".join(stack)