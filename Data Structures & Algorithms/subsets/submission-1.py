class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(path, start):
            res.append(path.copy())
            
            for idx in range(start, len(nums)):
                path.append(nums[idx]) #including/choose
                backtrack(path, idx + 1) #explore
                path.pop() #unchoose

        backtrack([], 0)
        return res