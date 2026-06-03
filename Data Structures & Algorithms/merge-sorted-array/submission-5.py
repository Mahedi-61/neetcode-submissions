class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0: return 

        nums1[m:] = nums2[::-1]


        j = 0
        i = 0
        while i < m + n:
            if j < len(nums2) and nums1[i] > nums2[j]:
                nums1[i : ] = [nums2[j]] + nums1[i : -1]
                j += 1

            else:
                i += 1