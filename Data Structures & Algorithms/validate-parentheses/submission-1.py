class Stack:
    def __init__(self):
        self.stack = []
        self.length = 0

    def push(self, val):
        self.length += 1
        self.stack.append(val)
        return True 

    def pull(self):
        if self.length == 0:
            return None 
        else:
            self.length -= 1
            return self.stack.pop()
    def is_empty(self):
        return True if self.length == 0 else False 

class Solution:
    def isValid(self, s: str) -> bool:
        stack = Stack()
        b_dict = {")": "(", "}": "{", "]" : "["}

        for c in s:
            if c in ["(", "{", "["]:
                stack.push(c)
            
            else:
                val = stack.pull()

                if val is None or val != b_dict[c]:
                    return False 

        return True if stack.is_empty() else False  