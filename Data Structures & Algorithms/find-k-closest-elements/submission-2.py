from collections import defaultdict

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        seen = defaultdict(list)

        for num in arr:
            key = abs(x - num)
            seen[key].append(num)

        keys = sorted(seen)
        c = 0
        res = []
        for s in keys:
            values = seen[s]

            if c + len(values) < k:
                res += values
                c += len(values)

            else:
                remainder = k - c
                res += sorted(values)[:remainder]
                break 

        return sorted(res)
    