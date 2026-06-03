class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        ls_greater = []
        ls_smaller = []
        for i in range(0, len(arr)-1):
            if i % 2 == 0 and arr[i] > arr[i+1]:
                ls_greater.append(1)
            elif i % 2 == 1 and arr[i] < arr[i + 1]:
                ls_greater.append(1)
            else:
                ls_greater.append(0)

        for i in range(0, len(arr)-1):
            if i % 2 == 0 and arr[i] < arr[i+1]:
                ls_smaller.append(1)

            elif i % 2 == 1 and arr[i] > arr[i + 1]:
                ls_smaller.append(1)
            else:
                ls_smaller.append(0)

        max_size = 0
        temp = 0
        for i in range(0, len(ls_greater)):
            if ls_greater[i] > 0:
                temp += 1
            else:
                max_size = max(max_size, temp)
                temp = 0
        max_size = max(max_size, temp)

        temp = 0
        for i in range(0, len(ls_smaller)):
            if ls_smaller[i] == 1:
                temp += 1
            else:
                max_size = max(max_size, temp)
                temp = 0
        max_size = max(max_size, temp)
        return max_size + 1 