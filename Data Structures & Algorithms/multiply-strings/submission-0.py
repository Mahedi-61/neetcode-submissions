class Solution:
    def str_to_int(self, str_nums):
        number = 0

        for char in str_nums:
            digit = ord(char) - ord('0')
            number = (number * 10) + digit
        return number

    def multiply(self, num1: str, num2: str) -> str:
        return str(self.str_to_int(num1) * self.str_to_int(num2))