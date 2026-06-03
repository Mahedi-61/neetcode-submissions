class Solution:
    def do_bin_sum(self, int_a, int_b):
        while(int_b != 0):
            carry = (int_a & int_b) << 1
            int_a = int_a ^ int_b 
            int_b = carry

        return int_a 

    def addBinary(self, a: str, b: str) -> str:
        int_a = int(a, 2)
        int_b = int(b, 2)
        bin_sum = self.do_bin_sum(int_a, int_b)
        return bin(bin_sum)[2:]