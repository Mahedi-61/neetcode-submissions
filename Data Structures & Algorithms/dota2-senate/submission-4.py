class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        ls_votes = [1] * len(senate)
        del_r = 0
        del_d = 0

        while True:
            total_r = 0
            total_d = 0

            for i, s in enumerate(senate):
                if ls_votes[i] == 0: 
                    continue

                elif s == "R":
                    if del_r > 0: 
                        del_r -= 1
                        ls_votes[i] = 0

                    else:
                        ls_votes[i] = 1
                        total_r += 1
                        del_d += 1

                else:
                    if del_d > 0:
                        del_d -= 1
                        ls_votes[i] = 0
                    else:
                        ls_votes[i] = 1
                        total_d += 1
                        del_r += 1

            if total_r == 0:
                return "Dire"
            elif total_d == 0:
                return "Radiant"
