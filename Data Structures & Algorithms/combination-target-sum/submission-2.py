class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(path, target, start):
            if target == 0:
                res.append(path.copy())
                return

            for i in range(start, len(nums)):
                if target - nums[i] < 0:
                    continue

                path.append(nums[i])
                # Stay at i because we can reuse the same element
                backtrack(path, target-nums[i], i)
                path.pop()

        backtrack([], target, 0)
        return res