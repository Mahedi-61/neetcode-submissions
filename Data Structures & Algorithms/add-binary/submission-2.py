class Solution:
    def get_digits(self, x):
        if x == 0: return [0]
        res = []
        while (x != 0):
            res.append(x % 10)
            x = x // 10
        return res

    def bin_addition(self, ls_a, ls_b):
        i = 0
        j = 0
        carry = 0
        res = []
        while i < len(ls_a) and j < len(ls_b):
            add = ls_a[i] + ls_b[j] + carry
            if add < 2:
                carry = 0
                res.append(str(add))
            elif add == 2:
                res.append(str(0))
                carry = 1
            elif add == 3:
                res.append(str(1))
                carry = 1 
        
            i += 1
            j += 1

        while i < len(ls_a):
            add = ls_a[i] + carry
            if add < 2:
                carry = 0
                res.append(str(add))
            elif add == 2:
                res.append(str(0))
                carry = 1
            i += 1

        while j < len(ls_b):
            add = ls_b[j] + carry
            if add < 2:
                carry = 0
                res.append(str(add))
            elif add == 2:
                res.append(str(0))
                carry = 1
            j += 1

        if carry == 1: res.append(str(1))
        return res

    def addBinary(self, a: str, b: str) -> str:
        int_a = int(a)
        int_b = int(b)

        ls_a = self.get_digits(int_a)
        ls_b = self.get_digits(int_b)
 
        bits = self.bin_addition(ls_a, ls_b)
        return "".join(bits[::-1])

        # num_a = 0
        # for i, num in enumerate(ls_a):
        #     num_a += num * (2**i)

        # num_b = 0
        # for i, num in enumerate(ls_b):
        #     num_b += num * (2**i)

        # return str(bin(num_a + num_b))[2:]