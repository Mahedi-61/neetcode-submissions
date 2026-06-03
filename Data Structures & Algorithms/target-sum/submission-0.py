class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        count =  0
        def dfs(i, amount):
            nonlocal count
            if i == len(nums):
                if amount == target:
                    count += 1
                    return
            
                elif amount != target:
                    return
                    
            dfs(i + 1, amount + nums[i]) 
            dfs(i + 1, amount - nums[i])

        dfs(0, 0) 
        return count