class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ls_asteroids = []

        for i in range(len(asteroids)):
            if asteroids[i] > 0: sign = True #pos
            else: sign = False #neg 

            if len(ls_asteroids) == 0:
                ls_asteroids.append(asteroids[i])
                num_sign = sign
            
            else:
                num_sign = True if ls_asteroids[-1] > 0 else False
                if num_sign == sign or num_sign == False:
                    ls_asteroids.append(asteroids[i])

                else:
                    while len(ls_asteroids) > 0 and abs(asteroids[i]) > abs(ls_asteroids[-1]) and ls_asteroids[-1] > 0:
                        del ls_asteroids[-1]

                    if len(ls_asteroids) == 0 or ls_asteroids[-1] < 0:
                        ls_asteroids.append(asteroids[i])

                    elif abs(asteroids[i]) == abs(ls_asteroids[-1]) and ls_asteroids[-1] > 0:
                        del ls_asteroids[-1]

                    elif abs(asteroids[i]) < abs(ls_asteroids[-1]):
                        continue

        return ls_asteroids