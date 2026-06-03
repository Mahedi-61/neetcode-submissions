class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        save_dict = set()
        l = 0

        for r in range(len(nums)):
            if r - l > k:
                save_dict.remove(nums[l])
                l += 1

            if nums[r] in save_dict:
                return True
            save_dict.add(nums[r])

        return False
