class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: return x 

        # # linear search O(n)
        # i = 1
        # while i*i <= x:
        #     i += 1

        # if i*i == x:
        #     return i 
        # else:
        #     return i-1

        # Binary Search
        left = 1
        right = x 
        while (left <= right):
            mid = (left + right) // 2
            if mid * mid == x:
                return mid 
            
            elif mid*mid < x:
                left = mid + 1

            else:
                if (mid-1)*(mid-1) <= x:
                    return mid-1
                else:
                    right = mid-1

