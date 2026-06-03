class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # originally sorted in ascending order. --> Binary search
        # all elements in the sorted rotated array nums are unique,
        # return the index of target within nums, or -1 if it is not present. --> Searching/Finidng pr
        # can you write an algorithm that runs in O(log n) time? --> Efficient Searching (BS)

        def binary_search(arr):
            if len(arr) == 0: return -1
            l = 0
            r = len(arr) - 1
            while l <= r:
                mid = (l + r) // 2
                if target > arr[mid]:
                    l = mid + 1
                elif target < arr[mid]:
                    r = mid - 1
                else:
                    return mid
            return -1

        l = 0
        r = len(nums) - 1
        right = r
        cut = 0

        while l < r:
            mid = (l + r) // 2
            if nums[r] >= nums[mid]:
                r = mid - 1

            elif nums[r] < nums[mid]:
                l = mid + 1

        if l + 1 < len(nums) and nums[l + 1] < nums[l]:
            cut = l + 1
        else:
            cut = l
        
        left_arr = nums[ : cut]
        right_arr = nums[cut : ]

        l_idx = binary_search(left_arr)
        r_idx = binary_search(right_arr)
        
        if l_idx == -1 and r_idx == -1:
            return -1

        elif l_idx == -1:
            return len(left_arr) + r_idx

        elif r_idx == -1:
            return l_idx





