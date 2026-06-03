class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # There will always be exactly one valid solution.
        # Your solution must use O(1) additional space.
        # sorted in non-decreasing order.
        # Note that index1 and index2 cannot be equal

        # binary search solution
        for i, num in enumerate(numbers):
            temp = target - num
            l = i + 1
            r = len(numbers) - 1

            while l <= r:
                mid = l + (r - l) // 2
                if temp > numbers[mid]:
                    l = mid + 1
                elif temp < numbers[mid]:
                    r = mid - 1
                else:
                    return [i + 1, mid + 1]