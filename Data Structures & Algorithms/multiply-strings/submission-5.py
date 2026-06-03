class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0': return '0'
        dt_num = {
            "1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
            "6": 6, "7": 7, "8": 8, "9": 9, "0": 0
        }

        def get_first_digit_prod(i):
            carry = 0
            j = len(num2) - 1
            res = []
            d1 = dt_num[num1[i]]

            while j >=0 or carry:    
                d2 = 0 if j < 0 else dt_num[num2[j]]
                d_sum = d1 * d2 + carry
                carry = d_sum // 10
                d_sum = d_sum % 10
                res.append(d_sum)
                j -= 1
            return res

        final_res = []
        for i in range(len(num1)-1, -1, -1):
            final_res.append(get_first_digit_prod(i)[::-1] + [0] * (len(num1) - 1 - i))

        max_len = len(final_res[-1])
        for i in range(len(num1)):
            final_res[i] =  [0]*(max_len - len(final_res[i])) + final_res[i]


        print(final_res)
        carry = 0
        result = ""
        for j in range(len(final_res[0])-1, -1, -1):
            row_sum = carry
            for row in final_res:
                row_sum += row[j]

            carry = row_sum // 10
            row_sum = row_sum % 10
            result += str(row_sum)

        if carry !=0: result += str(carry)
        return result[::-1]
            







