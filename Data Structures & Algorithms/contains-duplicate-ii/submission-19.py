class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_dict = {}
        for i, num in enumerate(nums):
            if num in num_dict:
                if abs(num_dict[num] - i) <= k:
                    return True

            num_dict[num] = i
        
        return False 