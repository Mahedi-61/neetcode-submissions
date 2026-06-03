class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1: return True
        elif len(hand) % groupSize != 0: return False

        counter = defaultdict(int)
        for card in hand:
            counter[card] += 1

        ls_cards = sorted(list(counter.keys()), reverse=True)
        while ls_cards:
            if len(ls_cards) < groupSize:
                return False
            
            cards = ls_cards[-groupSize:]
            for i in range(len(cards)-1):
                if cards[i] - cards[i+1] != 1:
                    return False

            for i in range(len(cards)):
                counter[cards[i]] -= 1
                if counter[cards[i]] == 0:
                    ls_cards.remove(cards[i])

        return True