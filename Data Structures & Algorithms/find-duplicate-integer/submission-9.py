class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ls_vals = set()
        for num in nums:
            if num not in ls_vals:
                ls_vals.add(num)
            else:
                return num

        