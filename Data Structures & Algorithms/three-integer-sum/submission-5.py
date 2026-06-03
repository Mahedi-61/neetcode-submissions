class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = len(nums) - 1
            while(l < r):
                array = [nums[i], nums[l], nums[r]]
                if sum(array) == 0:
                    result.append(array)
                    l += 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1 
                    
                elif sum(array) < 0:
                    l += 1
                elif sum(array) > 0:
                    r -= 1 


        return result

        #     for j in range(i+1, len(nums)):
        #         if j > i+1 and nums[j] == nums[j-1]:
        #             continue 
                
        #         k = j + 1 
        #         while(k < len(nums)):
        #             array = [nums[i], nums[j], nums[k]]

        #             if sum(array) == 0:
        #                 result.append(array)
        #                 break 
                    
        #             k += 1 
        #             while k < len(nums) and nums[k] == nums[k-1]:
        #                 k += 1
        # return result 