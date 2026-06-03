class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights)-1
        max_area = 0

        while i < j:
            if heights[i] < heights[j]:
                min_h = heights[i] 
                area = min_h * (j - i)
                i += 1
            else:
                min_h = heights[j]
                area = min_h * (j - i)
                j -= 1

            max_area = max(area, max_area)
        return max_area
        