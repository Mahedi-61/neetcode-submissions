class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for astrd in asteroids:
            while True:
                if not stack or stack[-1] < 0 or astrd > 0:
                    stack.append(astrd)
                    break

                elif stack[-1] == abs(astrd):
                    stack.pop()
                    break

                elif stack[-1] > abs(astrd):
                    break
                
                elif stack[-1] < abs(astrd):
                    stack.pop()

        return stack

                