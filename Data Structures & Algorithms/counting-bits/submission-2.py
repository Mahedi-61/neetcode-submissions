class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(0, n+1):
            count = 0
            while num:
                count += num & 1
                num >>= 1 
            res.append(count)

        return res