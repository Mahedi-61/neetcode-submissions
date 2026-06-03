class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}
        for num in nums:
            seen[num] = 1 + seen.get(num, 0)
        
        for val, cnt in seen.items():
            if cnt == 1:
                return val 
                
        # for num in nums:
        #     if nums.count(num) == 1:
        #         return num 

        # result = 0
        # for num in nums:
        #     result ^= num

        # return result