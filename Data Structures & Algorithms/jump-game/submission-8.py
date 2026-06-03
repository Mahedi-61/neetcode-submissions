class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        if nums[0] == 0: return False

        res = [False] * len(nums)
        res[-1] = True

        for i in range(len(nums)-2, -1, -1):
            if nums[i] == 0:
                continue

            else:
                for j in range(1, nums[i]+1):
                    if res[i + j] == True:
                        res[i] = True
                        break

        return res[0]