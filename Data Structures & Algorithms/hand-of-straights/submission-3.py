class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        #brute force solution
        # greedy approach
        count = defaultdict(int)
        for num in hand:
            count[num] += 1
        
        hand = list(set(hand))
        hand.sort()
        n = len(hand)

        #sliding window approach
        j = 0
        while j + groupSize - 1 < n:
            c = count[hand[j]]
            count[hand[j]] -= c

            for k in range(1, groupSize):
                if hand[j + k] - hand[j + k - 1] != 1:
                    return False

                if count[hand[j + k]] < c:
                    return False
                else:
                    count[hand[j + k]] -= c

            prev = j
            for k in range(groupSize):
                if count[hand[j + k]] > 0: 
                    j += k
                    break

            if prev == j:
                j += groupSize

        return j == n

        