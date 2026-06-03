class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # O(1) space
        max_freq = {}
        for num in nums:
            if num in max_freq:
                max_freq[num] += 1
            
            else:
                if len(max_freq) == 1:
                    key = list(max_freq.keys())[0]
                    max_freq[key] -= 1
                    
                    if max_freq[key] == 0:
                        del max_freq[key]
                else:
                    max_freq[num] = 1

        return list(max_freq.keys())[0]
