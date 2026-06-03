class Solution:
    def minEnd(self, n: int, x: int) -> int:
        def combination(n):
            return 2 ** n

        def dec_to_bin(x):
            deg = 1
            while x >= 2**deg:
                deg += 1
            
            res = [0] * deg
            deg -= 1

            while x > 0:
                if x >= 2**deg:
                    x -= 2**deg
                    res[deg] = 1
                deg -= 1
                if deg < 0: break
            return res

        def bin_to_dec(x):
            res = 0
            for i in range(len(x)):
                res += x[i] * 2**i
            return res 

        bits = dec_to_bin(x)
        com_res = combination(bits.count(0))
        
        if com_res >= n:
            bits_res = dec_to_bin(n-1)
            j = 0
            for i in range(len(bits)):
                if bits[i] == 0 and j < len(bits_res):
                    bits[i] += bits_res[j]
                    j += 1

        else:
            n -= 1
            bits_final= dec_to_bin(n)
            j = 0
            for i in range(len(bits)):
                if bits[i] == 0 and j < len(bits_final):
                    bits[i] += bits_final[j]
                    j += 1
            bits += bits_final[j:]

        return bin_to_dec(bits)