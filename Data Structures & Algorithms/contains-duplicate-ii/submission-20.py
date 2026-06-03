class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #slding window technique

        l = 0
        sl_dict = set()
        for r in range(len(nums)):
            if r - l > k:
                sl_dict.remove(nums[l])
                l = l + 1

            if nums[r] in sl_dict:
                return True
            else:
                sl_dict.add(nums[r])

        return False