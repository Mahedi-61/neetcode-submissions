class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Optimized solution (Prefix sum + Hash map)
        i = 0
        count = 0
        prefix_sum = defaultdict(int)
        ls_sums = []

        while i < len(nums): ##O(n)
            if i == 0: #O(n)
                j = 0
                temp = 0
                while j < len(nums):
                    temp += nums[j]
                    ls_sums.append(temp)
                    prefix_sum[temp] = 1 + prefix_sum.get(temp, 0)
                    j += 1

                if k in prefix_sum:
                    count += prefix_sum[k]

            else:
                prefix_sum[ls_sums[i-1]] -= 1
                if ls_sums[i-1] + k in prefix_sum: #O(1)
                    count += prefix_sum[ls_sums[i-1] + k]

            i += 1
        return count