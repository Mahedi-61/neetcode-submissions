class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1 or k == 0: return False 

        for i in range(len(nums)):
            start = max(0, i-k)

            for j in range(start, i):
                if nums[i] == nums[j]:
                    return True
        return False 