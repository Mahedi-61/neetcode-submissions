class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1 or k == 0: return False 

        # linear search O(n)
        # for i in range(len(nums)):
        #     start = max(0, i-k)
        #     end = min(len(nums)-1, i + k)

        #     for j in range(i+1, end+1):
        #         if nums[i] == nums[j]: return True
            
        #     for j in range(start, i):
        #         if nums[i] == nums[j]: return True
        
        # return False

        #     for j in range(start, end+1):
        #         if i != j and nums[i] == nums[j]:
        #             return True

        # return False

        for i in range(len(nums)):
            start = max(0, i-k)
            end = min(len(nums)-1, i + k)

            if nums[i] in nums[start : i]:
                return True
                
            # if nums[i] in nums[i+1 : end+1]:
            #     return True 

        return False
