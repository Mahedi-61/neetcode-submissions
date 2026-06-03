import sys
sys.setrecursionlimit(10**6)

class Solution:
    def get_pivot(self, my_list, start, end):
        pivot_idx = start
        swap = start     
        for i in range(pivot_idx + 1, end + 1):
            if my_list[i] < my_list[pivot_idx]:
                swap += 1 
                if i != swap:
                    my_list[i], my_list[swap] = my_list[swap], my_list[i]
        
        my_list[swap], my_list[pivot_idx] = my_list[pivot_idx], my_list[swap]
        return swap 
    
    def quick_sort(self, nums, left, right):
        if left < right:
            pivot = self.get_pivot(nums, left, right)

            left = self.quick_sort(nums, left, pivot-1)
            right = self.quick_sort(nums, pivot+1, right)

        return nums


    def quick_sort_using_mem(self, my_list):
        if len(my_list) <= 1: return my_list
        pivot = my_list[0]
        left = [x for x in my_list[1:] if x <= pivot]
        right = [x for x in my_list[1:] if x > pivot]
        return self.quick_sort_using_mem(left) + [pivot] + self.quick_sort_using_mem(right)

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1: return nums 
        #return self.quick_sort_using_mem(nums)
        return self.quick_sort(nums, 0, len(nums) - 1)