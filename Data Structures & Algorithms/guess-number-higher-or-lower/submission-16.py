# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n

        while l <= r:
            mid_num = (l + r) //2
            if guess(mid_num) == -1:
                r = mid_num - 1

            elif guess(mid_num) == 1:
                l = mid_num + 1

            elif guess(mid_num) == 0:
                return mid_num

        return mid_num