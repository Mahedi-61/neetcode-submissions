class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        rot = k % len(nums)
        if rot != 0:
            nums[:] = nums[-rot : ] + nums[ : len(nums)-rot]


        