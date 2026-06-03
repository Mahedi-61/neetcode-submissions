class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        i = 0
        dt_sen = {"R":0, "D":0}
        d_count = senate.count("D")
        temp_d = 0
        temp_r = 0
        r_count = senate.count("R")

        while not (temp_r == r_count or temp_d == d_count):
            if senate[i] == "R":
                if dt_sen["R"] < 0:
                    dt_sen["R"] += 1
                else:
                    dt_sen["D"] -= 1
                    temp_d += 1

            elif senate[i] == "D":
                if dt_sen["D"] < 0:
                    dt_sen["D"] += 1
                else:
                    dt_sen["R"] -= 1
                    temp_r += 1
            
            i  += 1
            i = i % len(senate)


        return "Radiant" if temp_d == d_count else "Dire"