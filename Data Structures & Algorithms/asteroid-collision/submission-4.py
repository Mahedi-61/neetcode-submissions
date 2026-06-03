class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            # handling collisions
            while stack and a < 0 and stack[-1] > 0:
                val = stack[-1] + a
                if val > 0:
                    a = 0
                elif val < 0:
                    stack.pop()
                else:
                    stack.pop()
                    a = 0

            if a != 0:
                stack.append(a)

        return stack
