class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        for num in nums:
            count_dict[num] = 1 + count_dict.get(num, 0)
        
        freq_array = [[] for _ in range(len(nums))]
        for num, count in count_dict.items():
            freq_array[count-1].append(num)

        res = []
        i = 0
        while i < k:
            val = freq_array.pop()
            if val != []:
                res += val
            i += len(val)

        return res[:k]