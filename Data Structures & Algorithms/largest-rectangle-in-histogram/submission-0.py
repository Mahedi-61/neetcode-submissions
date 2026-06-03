class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        i, j = 0, 0
        max_rec = heights[0]
        
        while j < len(heights):
            min_len = float('inf')
            while j < len(heights):
                min_len = min(heights[j], min_len)
                if min_len == 0: break

                l = j - i + 1
                max_rec = max(max_rec, l*min_len)
                j += 1

            i += 1
            j = i

        return max_rec