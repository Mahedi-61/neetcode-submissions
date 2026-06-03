class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # <, >
        i = 1
        max_size = 0
        count = 1

        while i < len(arr):
            if arr[i-1] < arr[i]:
                count += 1
            else:
                i += 1
                max_size = max(max_size, count)
                count = 1
                continue

            i += 1
            if i < len(arr) and arr[i-1] > arr[i]:
                count += 1
            else:
                max_size = max(max_size, count)
                count = 1
                continue
            i += 1

        max_size = max(max_size, count)

        # >, <
        count = 1
        i = 1
        while i < len(arr):
            if arr[i-1] > arr[i]:
                count += 1
            else:
                i += 1
                max_size = max(max_size, count)
                count = 1
                continue

            i += 1
            if i < len(arr) and arr[i-1] < arr[i]:
                count += 1
            else:
                max_size = max(max_size, count)
                count = 1
                continue
            i += 1

        max_size = max(max_size, count)
        return max_size