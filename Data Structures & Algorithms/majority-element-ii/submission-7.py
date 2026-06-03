class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        size = len(nums) // 3
        result = []
        if len(nums) < 3: return nums # crazy condition; doesn't make sense; go against the description
        if len(nums) < size: return result # real statement for handling edge case. MAKE SENSE

        # nums.sort()
        # count = 1
        # result = set()

        # for i in range(0, len(nums)-1):
        #     if nums[i] == nums[i + 1]:
        #         count += 1
        #     else:
        #         count = 1
            
        #     if count > size:
        #             result.add(nums[i])

        # return list(result)
            
        d = {}
        result = set()
        for num in nums:
            d[num] = 1 + d.get(num, 0)
            if d[num] > size:
                result.add(num)

        return list(result)
        