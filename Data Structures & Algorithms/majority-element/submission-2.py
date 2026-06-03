class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #return the majority element.
        #appears more than math.floor(n / 2) times in the array

        count = 1
        val = nums[0]
        for i in range(1, len(nums)):
            if val != nums[i]:
                if count == 1:
                    val = nums[i]
                else:
                    count -= 1
            else:
                count += 1

        return val

