class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def dfs(path, i):
            if i == n+1:
                if len(path) == k: res.append(path[:]) #1
                return

            path.append(i)
            dfs(path, i+1) 
            path.pop()
            dfs(path, i+1)

        res = []
        dfs([], 1)
        return res