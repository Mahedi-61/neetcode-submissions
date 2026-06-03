class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = len(nums1) - 1
        j = len(nums2) - 1
        k = m - 1

        while i >= 0:
            if j >= 0 and k >=0:
                if nums2[j] >= nums1[k]:
                    nums1[i] = nums2[j]
                    j -= 1
                else:
                    nums1[i] = nums1[k]
                    k -= 1
                
            elif j >= 0:
                nums1[i] = nums2[j]
                j -= 1

            i -= 1