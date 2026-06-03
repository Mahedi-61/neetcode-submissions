class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # There will always be exactly one valid solution.
        # Your solution must use O(1) additional space.
        # sorted in non-decreasing order.
        # Note that index1 and index2 cannot be equal

        #Two-pointer approach
        # l = 0
        # r = len(numbers) - 1
        # while l < r:
        #     temp = numbers[l] + numbers[r]
        #     if target < temp:
        #         r -= 1
        #     elif target > temp:
        #         l += 1

        #     else:
        #         return [l+1, r+1]

        # return []

        # hash map solution
        seen = {}
        for i, num in enumerate(numbers):
            if num in seen:
                return [seen[num], i + 1]
            else:
                temp = target - num
                seen[temp] = i + 1 