class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # find the pivot
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < nums[l]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                break

        pivot = l
        if target == nums[pivot]:
            return True
        elif target < nums[r]:
            l = pivot
            r = len(nums) - 1
        elif target > nums[r]:
            r = pivot - 1
            if r < 0: r = 0
            l = 0

        while l <= r:
            mid = (l + r) // 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return True

        return True if target in nums else False
