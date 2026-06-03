# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0

#def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
            left = 1 
            right = n

            while left <= right:
                i = (left + right) // 2
                #num = num_list[i]
                num = i
                check = guess(num)

                if check == 0: 
                    return num 

                elif check == -1: #higher
                    right = i - 1

                elif check == 1: #lower
                    left = i + 1

            return -1