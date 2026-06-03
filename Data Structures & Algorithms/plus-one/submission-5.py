class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        carry = 1
        i = len(digits) - 1

        while i >= 0 or carry:
            a = digits[i] if i >= 0 else 0
            total = a + carry

            if total > 9:
                carry = total // 10
                total = total % 10
            else:
                carry = 0

            res.append(total)
            i -= 1 

        return res[::-1]