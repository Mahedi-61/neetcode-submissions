class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # result[i] is the number of days after the ith day before a warmer temperature appears
        # no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

        res = [0] * len(temperatures)
        stack = []
        idx = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1]:
                stack.pop()
                j = idx.pop()
                res[j] = i - j

            stack.append(temp)
            idx.append(i)            

        return res 
