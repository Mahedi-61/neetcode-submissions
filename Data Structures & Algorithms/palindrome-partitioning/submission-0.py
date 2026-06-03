class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def palindrom(s1):
            l, r = 0, len(s1)-1
            while l <= r:
                if s1[l] != s1[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(path, temp):
            if temp == "":
                res.append(path[:])
                return

            for i in range(len(temp)):
                n_str = temp[ : i+1]
                if not palindrom(n_str):
                    continue

                path.append(n_str)
                backtrack(path, temp[i+1:])
                path.pop()
        
        res = []
        backtrack([], s)
        return res