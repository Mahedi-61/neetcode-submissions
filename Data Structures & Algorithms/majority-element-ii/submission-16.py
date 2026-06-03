class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # sol: O(1) space
        dt_count = {}
        count = len(nums) // 3

        # first pass
        for num in nums:
            if len(dt_count) == 2 and (num not in dt_count):
                all_keys = list(dt_count.keys())
                for key in all_keys:
                    dt_count[key] -= 1
                    if dt_count[key] == 0: del dt_count[key]
            else:
                dt_count[num] = dt_count.get(num, 0) + 1

        # second pass
        res = []
        for val in dt_count:
            if nums.count(val) > count:
                res.append(val)
        return res