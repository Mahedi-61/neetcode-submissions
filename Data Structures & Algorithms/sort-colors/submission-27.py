class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # in-place, one pass
        i, j, k = 0, 0, len(nums)-1
        while j <= k:
            if nums[k] == 2:
                k -= 1
            
            elif nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            
            elif nums[k] == 0:
                nums[i], nums[k] = nums[k], nums[i]
                i += 1
                j += 1

            elif nums[j] == 2:
                nums[k], nums[j] = nums[j], nums[k]

            else:
                j += 1