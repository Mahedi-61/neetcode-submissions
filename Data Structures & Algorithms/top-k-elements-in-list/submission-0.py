class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        for num in nums:
            count_dict[num] = 1 + count_dict.get(num, 0)
        
        values = sorted(list(count_dict.values()), reverse=True )[:k]
        res = []
        for i, j in count_dict.items():
            if j in values:
                res.append(i)
        return res[:k]