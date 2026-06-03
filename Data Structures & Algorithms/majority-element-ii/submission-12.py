class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        size = len(nums) // 3

        seen = {}
        res = set()
        for num in nums:
            seen[num] = 1 + seen.get(num, 0)

            if seen[num] > size:
                res.add(num)
        return list(res)