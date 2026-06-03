class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]: return True

            # mid is in left sorted array
            if nums[l] < nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            #mid is in right sorted array
            elif nums[r] > nums[mid]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

            elif nums[l] == nums[mid]:
                l += 1

            elif nums[r] == nums[mid]:
                r -= 1

        return False

            
