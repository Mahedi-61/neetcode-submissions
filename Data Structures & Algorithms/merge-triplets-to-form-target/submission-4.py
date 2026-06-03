class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if len(triplets) == 1:
            return triplets[0] == target
        
        first = False 
        second = False 
        third = False

        for tr in triplets:
            if target[0] < tr[0] or target[1] < tr[1] or target[2] < tr[2]:
                continue

            if target[0] == tr[0]: first = True
            if target[1] == tr[1]: second = True
            if target[2] == tr[2]: third = True

        return first and second and third