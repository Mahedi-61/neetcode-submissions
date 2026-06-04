class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #solving in O(1) space and in linear time
        store = [] #val, freq

        for num in nums:
            if not store or store[1] == 0:
                store = [num, 1]
            
            elif num == store[0]:
                store[1] += 1

            else:
                store[1] -= 1

        return store[0]
