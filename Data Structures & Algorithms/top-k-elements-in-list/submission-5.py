class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}
        freq_dict = defaultdict(list)

        for num in nums:
            num_dict[num] = 1 + num_dict.get(num, 0)

        for key, val in num_dict.items():
            freq_dict[val].append(key)

        values = sorted(freq_dict, reverse=True)

        res = []
        for val in values:
            res += freq_dict[val]
            if len(res) > k: break

        return res[:k]




        