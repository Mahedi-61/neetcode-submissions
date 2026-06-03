class Stack:
    def __init__(self):
        self.stack = []
        self.length = 0
    
    def push(self, val):
        self.stack.append(val)
        self.length += 1
        return True 

    def pop(self):
        if self.length > 0:
            self.length -= 1
            return self.stack.pop()
        return None 



class Solution:
    def checkValidString(self, s: str) -> bool:
        left_p = Stack()
        star = Stack()

        for i, c in enumerate(s):
            if c == "(":
                left_p.push(i)

            elif c == "*":
                star.push(i)

            else:
                if left_p.pop() is not None:
                    continue

                else:
                    if star.pop() is not None:
                        continue
                    else:
                        return False 

        while left_p.length > 0:
            idx_left = left_p.pop()
            idx_star = star.pop()
            if idx_star is None or idx_star < idx_left:
                return False

        return True