class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        dt_idx = {}
        for i, num in enumerate(nums):
            if num in dt_idx:
                if abs(i - dt_idx[num]) <= k:
                    return True

            dt_idx[num] = i
        return False