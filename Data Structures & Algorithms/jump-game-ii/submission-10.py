class Solution:
    def jump(self, nums: List[int]) -> int:
        #greddy solution (the best) O(n)
        l, r = 0, 0
        farthest = 0
        step = 0

        while r < len(nums)-1:
            step += 1
            for i in range(l, r+1):
                if nums[i] == 0:
                    continue

                farthest = max(farthest, nums[i] + i)

            l = r + 1
            r = farthest

        return step
    