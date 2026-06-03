class Solution:
    # Each boat carries at most two people at the same time, 
    # provided the sum of the weight of those people is at most limit.
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse = True)
        l = 0
        r = len(people) - 1
        cnt = 0

        while l < r:
            # loading 2 heaviest people
            remain = limit - people[l]
            l += 1
            cnt += 1

            if remain > 0:
                if people[l] <= remain:
                    l += 1
                elif people[r] <= remain:
                    r -= 1
        
        if l==r: cnt +=1 
        return cnt