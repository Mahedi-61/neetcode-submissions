class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x[0] == "-":
            x = int(x[0] + x[:0:-1])
            if x < -2**31:
                x = 0
        else:
            x = int(x[::-1])
            if x > 2**31 - 1:
                x =0 

        return x