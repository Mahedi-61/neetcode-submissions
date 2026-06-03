class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(path):
            if len(path) == len(nums):
                res.append([nums[i] for i in path[:]])
                return

            for idx in range(len(nums)):
                if idx in path:
                    continue

                if idx > 0 and idx-1 not in path and nums[idx-1] == nums[idx]:
                    continue

                path.append(idx)
                dfs(path)
                path.pop() 

        nums.sort()
        n = len(nums)
        res = []
        dfs([])
        return res