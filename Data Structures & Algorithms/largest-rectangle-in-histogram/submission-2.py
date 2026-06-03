class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #monotonically increasing stack
        stack = []
        i = 0
        max_area = heights[0]

        for idx, val in enumerate(heights):
            if not stack:
                stack.append([val, idx])
            
            elif stack[-1][0] < heights[idx]:
                stack.append([val, idx])

            else:
                if stack[-1][0] == heights[idx]: continue 
                
                top_idx = idx
                while stack and stack[-1][0] > heights[idx]:
                    top_val, top_idx = stack.pop()
                    max_area = max(max_area, top_val * (idx-top_idx))

                stack.append([val, top_idx])

        if stack:
            end = len(heights)
            while stack:
                top_val, top_idx = stack.pop()
                max_area = max(max_area, top_val * (end-top_idx))

        return max_area


            


