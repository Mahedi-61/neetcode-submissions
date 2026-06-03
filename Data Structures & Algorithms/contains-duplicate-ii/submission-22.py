class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 0 or k == 0:
            return False

        i = 0
        j = 1
        nums_dict = defaultdict(int)
        nums_dict[nums[i]] += 1

        while j < len(nums):
            if j - i <= k:
                if nums_dict[nums[j]] > 0:
                    return True
                else:
                    nums_dict[nums[j]] += 1
                j += 1

            else:
                nums_dict[nums[i]] -= 1
                i += 1

        return False