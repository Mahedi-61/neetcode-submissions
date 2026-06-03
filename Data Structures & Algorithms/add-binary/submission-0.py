class Solution:
    def get_digits(self, x):
        res = []
        while (x != 0):
            res.append(x % 10)
            x = x // 10
        return res

    def addBinary(self, a: str, b: str) -> str:
        int_a = int(a)
        int_b = int(b)

        ls_a = self.get_digits(int_a)
        ls_b = self.get_digits(int_b)
 
        num_a = 0
        for i, num in enumerate(ls_a):
            num_a += num * (2**i)

        num_b = 0
        for i, num in enumerate(ls_b):
            num_b += num * (2**i)

        return str(bin(num_a + num_b))[2:]