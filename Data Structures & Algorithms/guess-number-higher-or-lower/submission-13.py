# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0

#def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # Linear Search
        # i = 1
        # while i <= n:
        #     if guess(i) == 0:
        #         return i 
        #     i += 1

        # left = 1 
        # right = n

        # Binary Search
        # while left <= right:
        #     i = (left + right) // 2
        #     num = i
        #     check = guess(num)

        #     if check == 0: 
        #         return num 

        #     elif check == -1: #higher
        #         right = i - 1

        #     elif check == 1: #lower
        #         left = i + 1

        # return -1

        # Tenary Search
        l = 1
        r = n 
        while True:
            m1 = l + (r - l) // 3
            m2 = r - (r - l) // 3
            if guess(m1) == 0:
                return m1 
            elif guess(m2) == 0:
                return m2 
            
            if guess(m1) + guess(m2) == 0:
                l = m1 + 1
                r = m2 - 1

            elif guess(m1) == -1:
                r = m1 -1 
            else:
                l = m2 + 1