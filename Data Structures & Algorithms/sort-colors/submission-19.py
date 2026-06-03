class Solution:

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # sort the array in-place such that elements of the same color are grouped together
        # order: red (0), white (1), and then blue (2).
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        index = 0
        for n in range(3):
            if n in count:
                for _ in range(count[n]):
                    nums[index] = n
                    index += 1