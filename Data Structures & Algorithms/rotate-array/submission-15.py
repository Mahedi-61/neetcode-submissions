class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # not a pythonic solution
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        n = len(nums)
        k %= n
        if k == 0: return 
        # full reverse [d, c, b, a]
        reverse(0, n-1)

        # first k reverse[c, d, b, a]
        reverse(0, k-1)

        # rest part reverse
        reverse(k, n-1)