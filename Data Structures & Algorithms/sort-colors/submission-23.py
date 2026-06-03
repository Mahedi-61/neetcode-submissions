class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums) - 1
        i = 0
        two_cnt = 0
        while i < len(nums) - two_cnt:
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
            
            elif nums[i] == 2:
                while r > 0 and nums[r] == 2:
                    r -= 1
                    two_cnt += 1

                if r < i: break

                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
                two_cnt += 1

                if nums[i] == 0:
                    i -= 1

            i += 1
            print(nums)
           
