class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def dfs(path):
            if len(path) == len(nums): #base
                res.append(path.copy())
                return 

            for idx in range(len(nums)):
                if nums[idx] not in path:
                    path.append(nums[idx]) # choose 1, 2, 3
                    dfs(path) #explore 3
                    path.pop() #backtrack

        dfs(path)
        return res