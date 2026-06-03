class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        if m == 0:
            nums1[:] = nums2[:]
            return 

        elif n == 0:
            return 

        i = 0
        j = 0
        k = m
        val1 = m

        while j < n and i < m + n:
            if nums1[i] <= nums2[j]:
                i += 1
                val1 -= 1 

            if val1 == 0 and j < n:
                nums1[i:] = nums2[j:]
                break
            
            if j < n and i < m+n and nums2[j] < nums1[i]:
                nums1[i+1 : k+1] = nums1[i : k]
                nums1[i] = nums2[j]
                j += 1
                i += 1
                k += 1