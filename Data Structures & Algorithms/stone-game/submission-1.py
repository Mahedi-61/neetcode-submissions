class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        def dfs(res):
            if len(res) == 0:
                return 0

            if tuple(res) in memo:
                return memo[tuple(res)]

            alice_f = res[0] + max(dfs(res[2:]), dfs(res[1:-1]))
            alice_l = res[-1]  + max(dfs(res[1:-1]), dfs(res[:-2]))

            memo[tuple(res)] = max(alice_f, alice_l)
            return memo[tuple(res)]

        memo = {}
        alice_score = dfs(piles)
        bob_score = sum(piles) - alice_score

        return True if alice_score > bob_score else False