class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # sol: O(1) space
        # remove 3 distinct elements in a dict
        dt_count = {}
        count = len(nums) // 3
        
        for num in nums:
            if len(dt_count) == 2 and (num not in dt_count):
                all_keys = list(dt_count.keys())
                for key in all_keys:
                    dt_count[key] -= 1
                    if dt_count[key] == 0: del dt_count[key]
            else:
                dt_count[num] = dt_count.get(num, 0) + 1

        if not dt_count:
            return []
        else:
            for key in dt_count:
                dt_count[key] = 0
            for num in nums:
                if num in dt_count:
                    dt_count[num] += 1

        res = []
        for key in dt_count:
            if dt_count[key] > count:
                res.append(key)
        return res