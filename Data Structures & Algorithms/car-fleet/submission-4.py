class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        post = []

        for i in range(len(position)):
            t = (target - position[i]) / speed[i]
            post.append([position[i], t])

        post.sort(reverse=True)
        res = 0
        time = 0
        for j, pos in enumerate(post):
            if j == 0:
                time = pos[1]
                res = 1
            if pos[1] > time:
                res += 1
                time = pos[1]

        return res



