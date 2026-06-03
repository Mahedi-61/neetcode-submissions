class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if len(triplets) == 1:
            return triplets[0] == target
        
        set_idx = set()
        for i, trpl in enumerate(triplets):
            if target[0] == trpl[0] and target[1] >= trpl[1] and target[2] >= trpl[2]:
                set_idx.add(i)

            if target[1] == trpl[1] and target[0] >= trpl[0] and target[2] >= trpl[2]:
                set_idx.add(i)

            if target[2] == trpl[2] and target[1] >= trpl[1] and target[0] >= trpl[0]:
                set_idx.add(i)

        if not set_idx: return False
        final_trpl = [max(triplets[i][0] for i in set_idx),
                      max(triplets[i][1] for i in set_idx),
                      max(triplets[i][2] for i in set_idx)]

        return final_trpl == target