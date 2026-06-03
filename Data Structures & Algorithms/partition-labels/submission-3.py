class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter = defaultdict(int)
        for i,c in enumerate(s):
            counter[c] = i

        res = [] #substring len
        max_idx = 0
        j = 0

        for idx, c in enumerate(s):
            max_idx = max(max_idx, counter[c])

            if max_idx == idx:
                res.append(idx - j + 1) 
                max_idx = 0
                j = idx + 1

        return res