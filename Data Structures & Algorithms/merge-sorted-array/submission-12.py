class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if n == 0:
            return
        if m == 0:
            nums1[:] = nums2[:]

        nums1[m: ] = nums2[::-1]
        i, j = 0, 0
        while i < m + n and j < n:
            if nums1[i] > nums2[j]:
                nums1[:] = nums1[:i] + [nums2[j]] + nums1[i:-1]
                j += 1

            else:
                i += 1

        return nums1