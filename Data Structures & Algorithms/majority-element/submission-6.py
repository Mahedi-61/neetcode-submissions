class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # O(1) space
        can, count = nums[0], 0

        for num in nums:
            if num == can:
                count += 1

            elif count == 0:
                can = num
                count += 1

            else:
                count -= 1
        return can

