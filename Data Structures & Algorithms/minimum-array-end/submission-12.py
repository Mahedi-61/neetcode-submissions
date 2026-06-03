class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # bin of x and n-1
        # iterate 0's of x to place digits of n-1
        # res of the digists place after x form the bin --> int | return

        def get_bin(num):
            res = []
            while num:
                res.append(num & 1)
                num >>= 1
            return res #not reversing

        org_bin = get_bin(x)
        size_bin = get_bin(n-1)

        res = org_bin[:]
        i, j = 0, 0

        while i < len(org_bin) and  j < len(size_bin):
            if org_bin[i] == 0:
                res[i] = size_bin[j]
                j += 1

            i += 1

        if i == len(org_bin):
                res += size_bin[j :]

        res_str = [str(k) for k in res[::-1]]
        return int("".join(res_str), 2)
