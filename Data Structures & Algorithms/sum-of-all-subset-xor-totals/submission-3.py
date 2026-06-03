class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def dfs(i, path):
            if len(nums) == i:
                res.append(path[:])
                return

            path.append(nums[i])
            dfs(i+1, path)
            path.pop()
            dfs(i+1, path)

        res = []
        dfs(0, [])
        count = 0
        
        for r in res:
            c = 0
            for num in r:
                c ^= num
            count += c
        return count