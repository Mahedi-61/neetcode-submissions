class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def dfs(path, i):
            if len(path) == k: 
                res.append(path[:]) 
                return

            if (n + 1) - i < k - len(path):
                return 

            path.append(i)
            dfs(path, i+1) 
            path.pop()
            dfs(path, i+1)

        res = []
        dfs([], 1)
        return res