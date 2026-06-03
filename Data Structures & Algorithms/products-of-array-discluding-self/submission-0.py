class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #solving O(n) time with division operation

        total_sum = 1
        zeros = []
        for num in nums:
            if num != 0: total_sum *= num
            else: zeros.append(num)

        res = []
        for num in nums:
            if len(zeros) == 1 and num in zeros:
                res.append(total_sum)

            elif len(zeros) == 0:
                res.append(total_sum // num)

            else:
                res.append(0)
            
        return res