class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        # ans -> length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
        # Specifically, ans is the concatenation of two nums arrays.

        #return nums + nums
        ans = []
        n = len(nums)
        for i in range(2 * n):
            ans.append(nums[i % n])

        return ans