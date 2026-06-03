class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # memory: seen/memo O(1)
        memo = {}

        for i in range(len(nums)):
            if nums[i] in memo:
                return [memo[nums[i]], i]

            memo[target-nums[i]] = i

        