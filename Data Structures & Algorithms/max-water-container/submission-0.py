class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # brute-force soln
        res = 0
        for i in range(len(heights) - 1):
            row_max = 0
            for j in range(i + 1, len(heights)):
                temp = (j - i) * min(heights[i], heights[j])
                row_max = max(row_max, temp)

            res = max(res, row_max)
        return res