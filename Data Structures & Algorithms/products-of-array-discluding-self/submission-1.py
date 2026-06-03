class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #solving O(n) time with division operation

        # total_sum = 1
        # zeros = []
        # for num in nums:
        #     if num != 0: total_sum *= num
        #     else: zeros.append(num)

        # res = []
        # for num in nums:
        #     if len(zeros) == 1 and num in zeros:
        #         res.append(total_sum)

        #     elif len(zeros) == 0:
        #         res.append(total_sum // num)

        #     else:
        #         res.append(0)
            
        # return res

        #solving O(n) without division
        # frequency count
        res = [0] * len(nums)
        total = 1
        zero_count = 0

        for num in nums:
            if num == 0: zero_count += 1
            else:
                total = total * num

        if zero_count > 1:
            return res 

        for i, num in enumerate(nums):
            if zero_count == 1: 
                if num == 0: res[i] = total
            
            else:
                res[i] = total // num

        return res
        