class Solution:
    def countBits(self, n: int) -> List[int]:
        
        #brute force approach
        result = []
        for num in range(0, n+1):
            c = 0
            for i in range(32):
                if num & (1 << i) > 0:
                    c += 1
            result.append(c)

        return result