class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1

            while l < r:
                # while l > i+1 and nums[l] == nums[l-1]:
                #     l += 1
                #     if l == r: break
                # while r < len(nums)-1 and nums[r] == nums[r+1]:
                #     r -= 1
                #     if l == r: break
                # if l==r: break
                add = nums[i] + nums[l] + nums[r]
                if add == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif add < 0:
                    l += 1
                else:
                    r -= 1

        r = set()
        for i in res:
            r.add(tuple(i))
        return [list(j) for  j in r]