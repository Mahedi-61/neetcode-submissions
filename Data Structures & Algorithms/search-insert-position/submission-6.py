class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if target > nums[mid]:
                l += 1

            elif target < nums[mid]:
                r -= 1

            else:
                return mid

        if target > nums[l]:
            return l + 1
        
        elif target <= nums[l]:
            return l
