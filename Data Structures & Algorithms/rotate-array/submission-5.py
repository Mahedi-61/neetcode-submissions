class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        temp = [0] * len(nums)
        for i, num in enumerate(nums):
            temp[ (i + k) % len(nums) ] = num
        nums[:] = temp
        # rot = k % len(nums)
        # if rot != 0:
        #     nums[:] = nums[-rot : ] + nums[ : len(nums)-rot]

