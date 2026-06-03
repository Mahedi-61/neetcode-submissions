class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if not stack or stack[-1] < 0 or a > 0:
                stack.append(a)
                continue

            while stack[-1] > 0 and a < 0:
                if stack[-1] > abs(a):
                    break 

                elif stack[-1] < abs(a):
                    stack.pop()
                    if not stack or stack[-1] < 0: 
                        stack.append(a)
                        break
                else:
                    stack.pop()
                    break 

        return stack