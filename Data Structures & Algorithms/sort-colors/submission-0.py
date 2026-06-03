class Solution:
    def merge(self, list1, list2):
        combined = []
        i = 0
        j = 0
        while(i < len(list1) and j < len(list2)):
            if list1[i] < list2[j]:
                combined.append(list1[i])
                i += 1
            else:
                combined.append(list2[j])
                j += 1

        if i < len(list1):
            combined += list1[i:]

        if j < len(list2):
            combined += list2[j:]
        return combined 

    def merge_sort(self, nums):
        if len(nums) < 2: return nums

        mid = len(nums) // 2
        left = self.merge_sort(nums [ : mid])
        right = self.merge_sort(nums [mid : ])
        return self.merge(left, right)

    def sortColors(self, nums: List[int]) -> None:
        nums[:] = self.merge_sort(nums)