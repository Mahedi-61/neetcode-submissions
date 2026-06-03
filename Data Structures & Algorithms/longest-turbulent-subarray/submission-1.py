class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # comparison sign flips between each adjacent pair of elements in the subarray.
        def find_max_ones(arr):
            max_count = 0
            temp = 0
            for i, a in enumerate(arr):
                if a == 1:
                    temp += 1
                else:
                    max_count = max(max_count, temp)
                    temp = 0
            return max(max_count, temp)


        res_g = [0] * (len(arr) - 1)
        res_s = [0] * (len(arr) - 1)

        for i in range(1, len(arr)):
            if arr[i - 1] > arr[i]:
                res_g[i-1] = 1
            
            if arr[i - 1] < arr[i]:
                res_s[i-1] = 1

        res_1 = []
        res_2 = []
        for i in range(len(res_g)):
            if i % 2 == 0:
                res_1.append(res_g[i])
                res_2.append(res_s[i])
            else:
                res_1.append(res_s[i])
                res_2.append(res_g[i])

        print(res_1)
        print(res_2)
        return max(find_max_ones(res_1), find_max_ones(res_2)) + 1 
        