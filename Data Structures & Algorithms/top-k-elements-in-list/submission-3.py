class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        for num in nums:
            count_dict[num] = 1 + count_dict.get(num, 0)
        
        res = []
        for i, j in count_dict.items():
            res.append([j, i])
        
        res.sort()
        return [res.pop()[1] for i in range(k)]

