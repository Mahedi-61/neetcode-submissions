class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # (+, -) hit 
        # (+, +), (-, -), (-, +) no hit
        stack = []
        for ast in asteroids:
            if (not stack) or ast > 0:
                stack.append(ast)
            
            elif stack[-1] < 0 and ast < 0:
                stack.append(ast)
                pass

            else:
                flag = True
                while stack and stack[-1] > 0 and ast < 0:
                    if stack[-1] < abs(ast):
                        stack.pop()

                    elif stack[-1] > abs(ast):
                        flag = False
                        break
                    else:
                        stack.pop()
                        flag = False
                        break

                if flag: stack.append(ast)

        return stack