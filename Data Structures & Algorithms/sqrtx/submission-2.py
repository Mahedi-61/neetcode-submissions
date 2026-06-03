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

        # Binary Search O(log_2(n))
        # left = 1
        # right = x 
        # while (left <= right):
        #     mid = (left + right) // 2
        #     if mid * mid == x:
        #         return mid 
            
        #     elif mid*mid < x:
        #         left = mid + 1

        #     else:
        #         if (mid-1)*(mid-1) <= x:
        #             return mid-1
        #         else:
        #             right = mid-1


        # Tenary Search
        l = 1
        r = x 
        while( l <= r):
            mid1 = l + (r - l) // 3
            mid2 = r - (r - l) // 3

            if (mid1*mid1 == x):
                return mid1 
            elif mid1*mid1 > x and (mid1-1)*(mid1-1) <= x:
                return mid1-1

            if (mid2 * mid2 == x):
                return mid2 
            elif mid2*mid2 > x and (mid2-1)*(mid2-1) <= x:
                return mid2-1
                
            if mid1*mid1 < x and mid2*mid2 > x:
                l = mid1 + 1
                r = mid2 - 1

            elif mid1*mid1 > x:
                r = mid1 - 1

            elif mid2*mid2 < x:
                l = mid2 + 1
