import math
class Solution:
    # The operands may be integers or the results of other operations.
    # The operators include '+', '-', '*', and '/'.
    # Assume that division between integers always truncates toward zero.

    def evalRPN(self, tokens: List[str]) -> int:
        record = []
        total = 0
        
        for t in tokens:
            if t == "+":
                temp_sum = record.pop() + record.pop()
              
            elif t == "-":
                b = record.pop()
                a = record.pop()
                temp_sum = a - b

            elif t == "*":
                b = record.pop()
                a = record.pop()
                temp_sum = a * b

            elif t == "/":
                b = record.pop()
                a = record.pop()

                temp_sum = a / b
                temp_sum = math.floor(temp_sum) if temp_sum >= 0 else math.ceil(temp_sum)

            else:
                temp_sum = int(t)
            
            record.append(temp_sum)
        
        return record[-1]