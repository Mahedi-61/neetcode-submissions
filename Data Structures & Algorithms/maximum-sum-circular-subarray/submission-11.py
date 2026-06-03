class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        i = 0
        curr_sum = 0
        max_sum = nums[i]

        while i < len(nums):
            curr_sum += nums[i]
            j = i + 1
            idx = j % len(nums)

            if curr_sum + nums[idx] >= nums[idx]:
                while curr_sum + nums[idx] >= nums[idx]:
                    print(i, j)
                    if j - i < len(nums):
                        curr_sum += nums[idx]
                        max_sum = max(max_sum, curr_sum)
                        j += 1
                        idx = j % len(nums)
                    
                    else:
                        break
                curr_sum = 0
                i += 1

            else:
                curr_sum = 0
                max_sum = max(max_sum, nums[j % len(nums)])
                i += 1


        return max_sum