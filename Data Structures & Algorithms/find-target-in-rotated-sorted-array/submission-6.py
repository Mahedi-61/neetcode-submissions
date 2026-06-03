class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # finding pivot
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < nums[l]:
                l += 1
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                break
        
        pivot = l
        if nums[l] <= target <= nums[r]:
            pass
        else:
            l = 0
            r = pivot - 1
            if r < 0: r = 0

        while l <= r:
            mid = (l + r) // 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid
        return -1




