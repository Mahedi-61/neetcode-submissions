class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            for s in stack:
                s[1] += 1

            while stack and temperatures[stack[-1][0]] < temperatures[i]:
                idx, day = stack.pop()
                res[idx] = day

            stack.append([i, 0])

        return res
            

