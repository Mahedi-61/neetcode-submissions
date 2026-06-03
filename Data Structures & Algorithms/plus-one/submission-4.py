class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        carry = 1
        i = len(digits) - 1

        while i >= 0:
            temp = digits[i] + carry

            digits[i] = temp % 10
            carry = temp // 10
            i -= 1
        
        if carry != 0:
            return [carry] + digits
        return digits