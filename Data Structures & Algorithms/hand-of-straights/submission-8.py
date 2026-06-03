class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1: return True
        if len(hand) % groupSize != 0: return False

        dict_num = defaultdict(int)
        for num in hand:
            dict_num[num] += 1

        nums = sorted(dict_num.keys())

        k = 0
        while k < len(nums):
            start = True
            a = nums[k]

            for i, idx in enumerate(range(k, k + groupSize)):
                if idx == len(nums) or dict_num[nums[idx]] <= 0 or nums[idx] != a + i:
                    return False

                dict_num[nums[idx]] -= 1

                if dict_num[nums[idx]] > 0 and start:
                    start = False
                    k = idx
            
            if start: k += groupSize 

        return True
