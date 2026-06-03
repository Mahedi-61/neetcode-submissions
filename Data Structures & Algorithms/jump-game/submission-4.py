class Solution:
    def canJump(self, nums: List[int]) -> bool:
        status = len(nums)-1

        for i in range(len(nums)-2, -1, -1):
            for j in range(1, nums[i] + 1):
                if i + j >= status:
                    status = i
                    break

        return True if status == 0 else False

