class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        for d in digits:
            number = (number * 10) + d

        number += 1
        res = []
        while number:
            res.append(number % 10)
            number = number // 10

        return res[::-1] 