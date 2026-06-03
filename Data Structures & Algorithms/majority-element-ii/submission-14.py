class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # sol: O(n) space
        res = set()
        count = len(nums) // 3
        dt_num = {}

        for num in nums:
            if num not in res:
                dt_num[num] = dt_num.get(num, 0) + 1
                if dt_num[num] > count:
                    res.add(num)

        return list(res)