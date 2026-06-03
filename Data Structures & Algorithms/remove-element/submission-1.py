class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #optimized solution
        # two pointers
        j = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1

        return j