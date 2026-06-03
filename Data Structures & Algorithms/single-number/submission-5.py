class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # O(n) time O(1) space solution
        res = 0
        for num in nums:
            res ^= num

        return res


        # O(n) time O(n) space solution
        seen = set()
        for num in nums:
            if num in seen:
                seen.discard(num)
            else:
                seen.add(num)

        return seen[-1]