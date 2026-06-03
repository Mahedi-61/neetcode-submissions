class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1 or k == 0: return False 
        seen = set()
        l = 0
        for i in range(len(nums)):
            if i - l > k:
                seen.remove(nums[l])
                l += 1

            if nums[i] in seen:
                return True 

            seen.add(nums[i])
        return False