class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])
        load = 0

        i = 0
        while i < len(trips):
            load = trips[i][0]
            k = 1
            while i + k < len(trips) and trips[i + k][1] < trips[i][2]:
                    load += trips[i + k][0]
                    k += 1

            if load <= capacity:
                i += 1

            else:
                return False

        return True
