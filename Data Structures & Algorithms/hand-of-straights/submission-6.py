class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1: return True
        elif len(hand) % groupSize != 0: return False

        counter = defaultdict(int)
        for num in hand:
            counter[num] += 1

        ls_cards = sorted(list(counter))
        idx = 0

        while idx < len(ls_cards):
            if idx + groupSize - 1 >= len(ls_cards):
                return False

            for i in range(idx, idx + groupSize-1):
                if ls_cards[i+1] - ls_cards[i] == 1:
                    pass
                else:
                    return False

            dup = False
            mid_idx = 0
            for i in range(idx, idx + groupSize):
                card = ls_cards[i]

                if counter[card] == 0:
                    return False
                else:
                    counter[card] -= 1
                    if counter[card] > 0:
                        if not dup: mid_idx = i
                        dup = True
        
            if dup: idx = mid_idx
            else: idx = i + 1
        
        return True
