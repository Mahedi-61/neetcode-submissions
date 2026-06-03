class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        data_idx = {}
        for idx, num in enumerate(nums):
            if num in data_idx:
                if idx - data_idx[num] <= k:
                    return True

            data_idx[num] = idx
        
        return False