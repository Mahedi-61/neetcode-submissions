class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #two pointer solution -- linear/O(1)

        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l] == val:
                while r > l and nums[r] == val:
                    r -= 1
                
                if l == r: break
                else:
                    nums[l] = nums[r]
                    l += 1
                    r -= 1

            else:
                l += 1

        return l