class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #counter with indices (last)
        counter = {}
        for i, c in enumerate(s):
            counter[c] = i

        i = 0
        res = []
        while i < len(s):
            j = i
            last_idx = counter[s[i]]

            while j < len(s):
                last_idx = max(last_idx, counter[s[j]])
                if j == last_idx:
                    break
                j += 1

            print(i,j)
            res.append(j - i + 1)
            i = j + 1

        return res