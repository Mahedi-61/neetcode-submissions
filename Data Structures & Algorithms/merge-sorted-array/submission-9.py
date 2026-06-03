class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:] = nums2[:]
            return
        elif n == 0:
            return

        nums1[:] = nums1[-n:] + nums1[:m]
        i = n
        j, k = 0, 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums1[k] = nums1[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1

            k += 1
        
        if i == len(nums1):
            nums1[k:] = nums2[j:]