class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def Counter(ls):
            r = collections.defaultdict(int)
            for l in ls:
                r[l] += 1
            return r

        #recursive solution
        def dfs(target_sum, path):
            if target_sum == 0:
                res.append(path[:]) #adding
                return

            for num in nums:
                if target_sum - num >= 0:
                    path.append(num)
                    dfs(target_sum - num, path) #choose and explore
                    path.pop() #back

        res = []
        path = []
        dfs(target, path)
        uniq_res = []
        s = []
        for r in res:
            r_dict = Counter(r)
            if r_dict not in s:
                s.append(r_dict)
                uniq_res.append(r)

        return uniq_res