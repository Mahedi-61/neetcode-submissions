class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) -1 

        while(l < r):
            add_num = numbers[l] + numbers[r]
            if add_num == target:
                return [l+1, r+1]

            elif add_num < target:
                l += 1 

            else:
                r -= 1
