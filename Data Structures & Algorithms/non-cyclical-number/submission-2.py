class Solution:
    def isHappy(self, n: int) -> bool:
        #replace it with the sum of the squares of its digits.
        #If it stops at 1, then the number is a non-cyclical number.
        # return true if it is a non-cyclical number

        all_sums = set()
        def get_digits_sum(n):
            ls_digits = []
            while n:
                ls_digits.append(n % 10)
                n = n // 10
            return sum(digit**2 for digit in ls_digits)
        
        #brute-force solution  
        def check_others(d_sum):
            if d_sum in all_sums:
                return True
            return False

        while True:
            d_sum = get_digits_sum(n)
            if d_sum == 1:
                return True

            else:
                if check_others(d_sum) == True:
                    return False
                all_sums.add(d_sum)
                n = d_sum
