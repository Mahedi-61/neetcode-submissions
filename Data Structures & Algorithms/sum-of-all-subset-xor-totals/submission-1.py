class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # solving with dfs

        def dfs(path, step):
            if step == len(nums):
                res.append(path[:])
                return

            dfs(path, step + 1)

            path.append(nums[step])
            dfs(path, step + 1)
            path.pop()

        res = []
        path = []
        dfs([], 0)
        
        res_sum = 0
        for ele in res:
            if ele:
                if len(ele) == 1:
                    res_sum += ele[0]
                else:
                    temp = 0
                    for j in ele:
                        temp ^= j
                    res_sum += temp
        return res_sum    