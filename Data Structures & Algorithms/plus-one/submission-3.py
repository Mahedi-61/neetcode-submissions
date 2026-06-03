class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # number = 0
        # for d in digits:
        #     number = (number * 10) + d

        # number += 1
        # res = []
        # while number:
        #     res.append(number % 10)
        #     number = number // 10

        # return res[::-1] 

        i = len(digits) - 1 
        if digits[i] < 9:
            digits[i] += 1
            return digits

        while i >= 0 and digits[i] == 9:
            digits[i] = 0 
            i -= 1
        if digits[0] == 0:
            return [1] + digits
        else:
            digits[i] += 1 
            return digits
