class Solution:
    def countBits(self, n: int) -> List[int]:
        def bit_count(num):
            count = 0
            while num:
                if num & 1:
                    count += 1
                num = num >> 1
            return count

        res = []
        for i in range(0, n+1):
            res.append(bit_count(i))

        return res