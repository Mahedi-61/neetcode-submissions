class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        m_ele = nums[0]
        m_count = 0
        nums_dict = defaultdict(int)

        for num in nums:
            nums_dict[num] += 1

            if nums_dict[num] > m_count:
                m_count = nums_dict[num]
                m_ele = num
        
        return m_ele