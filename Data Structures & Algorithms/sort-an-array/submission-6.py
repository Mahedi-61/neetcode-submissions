import sys
sys.setrecursionlimit(10**6)

class Solution:
    def merge(self, list1, list2):
        i = 0 
        j = 0
        res = []

        while(i < len(list1) and j < len(list2)):
            if list1[i] < list2[j]:
                res.append(list1[i])
                i += 1
            else:
                res.append(list2[j])
                j += 1

        
        if i < len(list1):
            res += list1[i:]
        if j < len(list2):
            res += list2[j:]

        return res 

    def merge_sort(self, nums):
        if len(nums) < 2: return nums 
        mid = len(nums) // 2

        left = self.merge_sort(nums[:mid])         
        right = self.merge_sort(nums[mid:])       
        return self.merge(left, right)  


    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1: return nums 
        return self.merge_sort(nums)