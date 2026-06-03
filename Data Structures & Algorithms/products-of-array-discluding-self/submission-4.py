class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # time: O(n) & space: O(n)
        prefix_mul = defaultdict(int)
        prefix_mul[0] = nums[0]

        for i in range(1, len(nums)):
            prefix_mul[i] = prefix_mul[i - 1] * nums[i]

        suffix_mul = defaultdict(int)
        suffix_mul[len(nums)-1] = nums[-1]

        for i in range(len(nums)-2, -1, -1):
            suffix_mul[i] = suffix_mul[i + 1] * nums[i] 

        result = []
        for i in range(len(nums)):
            if i == 0:
                result.append(suffix_mul[i + 1])

            elif i == len(nums) - 1:
                result.append(prefix_mul[i - 1])

            else:
                result.append(prefix_mul[i - 1] * suffix_mul[i + 1])

        return result