class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] <= 0: continue

            if nums[i] > 1:
                    if i-1 < 0: return 1
                    elif nums[i-1] < 0: return 1
                    elif nums[i-1] > 0 and nums[i] - nums[i-1] > 1:
                        return nums[i-1] + 1

            elif (nums[i] > 0 and nums[i-1] == 0) and nums[i] - nums[i-1] > 1:
                return 1

            elif (nums[i] > 0 and nums[i-1] < 0) and nums[i] > 1:
                return 1

        if nums[-1] > 0:
            return nums[-1] + 1
        else:
            return 1