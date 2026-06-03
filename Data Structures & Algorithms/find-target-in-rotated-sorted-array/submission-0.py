class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # originally sorted in ascending order. --> Binary search
        # all elements in the sorted rotated array nums are unique,
        # return the index of target within nums, or -1 if it is not present. --> Searching/Finidng pr
        # can you write an algorithm that runs in O(log n) time? --> Efficient Searching (BS)

        #Trivial solution O(n)
        for i, num in enumerate(nums):
            if num == target:
                return i
        return -1
        
        