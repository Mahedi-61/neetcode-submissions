class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}

        for num in nums:
            num_dict[num] = 1 + num_dict.get(num, 0)

        freq_ls = [[] for _ in nums]

        for key, val in num_dict.items():
            freq_ls[val - 1].append(key)

        count = 0
        res = []
        while count < k:
            ls = freq_ls.pop()
            if ls:
                res += ls
                count += len(ls)

        return res[:k]