class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def bs(arr):
            i, j = 0, len(arr) - 1
            while i <= j:
                mid = (i + j) // 2
                if arr[mid] > target:
                    j -= 1

                elif arr[mid] < target:
                    i += 1

                else:
                    return mid
            return -1

        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        l, r = 0, len(nums)-1
        arr = []
        left_arr = []
        right_arr = []

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            elif nums[mid] < nums[l]:
                l += 1

            elif nums[mid] > nums[r]:
                r -= 1

            elif nums[l] <= nums[mid] and nums[mid] <= nums[r]:
                if l > 0 and r == len(nums)-1:
                    left_arr = nums[0: l]
                    right_arr = nums[l :]

                if l == 0 and r < len(nums)-1:
                    left_arr = nums[: r+1]
                    right_arr = nums[r+1 : ]

                if l == 0 and r == len(nums)-1:
                    left_arr = nums
                break

        l_idx, r_idx = -1, -1

        if len(left_arr) > 0:
            l_idx = bs(left_arr) 

        if l_idx != -1: return l_idx
        if len(right_arr) > 0:
            r_idx = bs(right_arr)

        if r_idx != -1: return len(left_arr) + r_idx
        return -1

