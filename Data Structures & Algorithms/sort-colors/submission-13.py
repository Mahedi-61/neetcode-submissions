class Solution:
    def merge_list(self, a, b):
        if len(a) == 0: return b
        elif len(b) == 0: return a 

        i = 0
        j = 0
        m_list = []
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                m_list.append(a[i])
                i += 1
            else:
                m_list.append(b[j])
                j += 1

        if i < len(a):
            m_list += a[i : ]
        elif j < len(b):
            m_list += b[j : ]
        return m_list

    def merge_sort(self, nums):
        if len(nums) < 2: return nums
        mid = len(nums) // 2
        left = self.merge_sort(nums[ : mid])
        right = self.merge_sort(nums[mid : ])
        return self.merge_list(left, right)


    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # sort the array in-place such that elements of the same color are grouped together
        # order: red (0), white (1), and then blue (2).

        nums[:] = self.merge_sort(nums)