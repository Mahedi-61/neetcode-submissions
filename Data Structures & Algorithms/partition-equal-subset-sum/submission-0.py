class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        status = False
        def dfs(path, start):
            nonlocal status
            if start == len(nums):
                if sum(path) == sum(nums) //2:
                    status = True
                return

            path.append(nums[start])
            dfs(path, start + 1)
            path.pop()
            dfs(path, start + 1)


        dfs([], 0)
        return status