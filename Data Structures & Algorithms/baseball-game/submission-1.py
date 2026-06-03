class Solution:
    # An integer x: Record a new score of x.
    # '+': Record a new score that is the sum of the previous two scores.
    # 'D': Record a new score that is the double of the previous score.
    # 'C': Invalidate the previous score, removing it from the record.
    # Return the sum of all the scores


    def calPoints(self, operations: List[str]) -> int:
        record = []

        for op in operations:
            if len(record) == 0 and op in ["C", "D", "+"]:
                continue
            
            if op == "C":
                del record[-1]
            
            elif op == "D":
                record.append(record[-1] * 2)

            elif op == "+":
                record.append(record[-1] + record[-2])
            
            else:
                record.append(int(op))

        return sum(record)
            

        