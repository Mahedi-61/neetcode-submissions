class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # brute-force soln
        # res = 0
        # for i in range(len(heights) - 1): # O(n**2)
        #     row_max = 0
        #     for j in range(i + 1, len(heights)):
        #         temp = (j - i) * min(heights[i], heights[j])
        #         row_max = max(row_max, temp)

        #     res = max(res, row_max)
        # return res

        i = 0
        j = len(heights)-1
        max_area = 0

        while i < j:
            area = (j - i) * min(heights[i], heights[j])
            max_area = max(area, max_area)

            if heights[i] <= heights[j]:
                i += 1

            else:
                j -= 1

        return max_area