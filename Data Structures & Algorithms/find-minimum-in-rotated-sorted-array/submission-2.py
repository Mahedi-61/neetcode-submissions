class Solution:
    def findMin(self, nums: List[int]) -> int:
        #3,4,5, 6,1,2
        #4,5,6,7
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                return res

            mid = (l + r) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        
        return res
