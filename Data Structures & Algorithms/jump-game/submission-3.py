class Solution:
    def canJump(self, nums: List[int]) -> bool:
        status = set()
        status.add(len(nums)-1)

        for i in range(len(nums)-2, -1, -1):
            for j in range(1, nums[i] + 1):
                if i + j in status:
                    status.add(i)

        return True if 0 in status else False

