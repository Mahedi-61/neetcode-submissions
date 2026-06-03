class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        if nums[0] == 0: return False

        reach = len(nums) - 1

        for i in range(len(nums)-2, -1, -1):
            if nums[i] == 0:
                continue

            elif i + nums[i] >= reach:
                reach = i

        return reach == 0