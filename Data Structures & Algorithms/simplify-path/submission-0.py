class Solution:
    def simplifyPath(self, path: str) -> str:
        # Any sequence of periods treated as a valid directory or file name
        # '//' and '///' are treated as a single slash '/'.
        # The path must not have any single or double periods ('.' and '..') 
        # The path must not end with a slash '/', unless it is the root directory. 

        path = path.split("/")
        inp = []
        for p in path:
            if p == "":
                continue
            inp.append(p)

        res_stack = []
        for temp in inp:
            if temp in ["..", "."]:
                if len(res_stack) != 0 and temp == "..":
                    res_stack.pop()
            else:
                res_stack.append(temp)

        return "/" + "/".join(res_stack)