class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        for num in nums:
            count_dict[num] = 1 + count_dict.get(num, 0)
        
        res = []
        for i, j in count_dict.items():
            res.append([j, i])
        
        res.sort(reverse=True)
        return [el for c, el in res][:k]

