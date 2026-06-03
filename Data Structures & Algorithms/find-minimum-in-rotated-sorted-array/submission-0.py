class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # efficient solution --> BS == O(log n)
        l = 0
        r = len(nums) - 1
        right = r

        while l < r:
            mid = (l + r) // 2
            if nums[right] >= nums[mid]:
                r = mid - 1

            elif nums[right] < nums[mid]: # 2 < 4
                l = mid + 1

        if l + 1 < len(nums) and nums[l + 1] < nums[l]:
            return nums[l + 1]
        else:
            return nums[l] 