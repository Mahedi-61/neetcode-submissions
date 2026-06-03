class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #return the majority element.
        #appears more than math.floor(n / 2) times in the array

        count = 0
        for num in nums:
            if count == 0:
                val = num
            count += 1 if val == num else -1

        return val