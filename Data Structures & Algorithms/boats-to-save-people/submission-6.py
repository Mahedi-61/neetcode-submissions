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
            if people[l] + people[l + 1] <= limit:
                l +=2 

            elif people[l] + people[r] <= limit:
                l += 1
                r -= 1

            else:
                if people[l] >= people[r] + people[r - 1]:
                    l += 1

                elif people[r] + people[r-1] <= limit:
                    r -= 2

                else:
                    l += 1

            cnt += 1 

        if l == r: cnt += 1
        return cnt 