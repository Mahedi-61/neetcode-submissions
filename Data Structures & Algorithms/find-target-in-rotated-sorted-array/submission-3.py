class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # dividive the array in two sorted parts O(log_n)
        # find out the interested parts O(1)
        # do binary search O(log_n)

        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[l]:
                r = mid 
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                break
        

        #short sorted list begin with l
        if l != 0:
            r = len(nums) - 1
            if target == nums[l]: return l
            elif nums[r] >= target >= nums[l]: 
               pass
            else:
                r = l - 1
                l = 0 

        while l <= r:
            mid = (l + r) // 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid

        return -1 