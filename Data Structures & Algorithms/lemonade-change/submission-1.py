class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        saved_m = {"5":0, "10":0, "20":0}

        for b in bills:
            if b > 5:
                rest = b - 5
                if rest == 5 and saved_m[str(rest)] > 0:
                    saved_m[str(rest)] -= 1

                elif rest == 15 and saved_m["5"] > 0 and saved_m["10"] > 0:
                    saved_m["10"] -= 1
                    saved_m["5"] -= 1

                elif rest == 15 and saved_m["5"] > 2:
                    saved_m["5"] -= 3

                else:
                    return False

            saved_m[str(b)] += 1
        return True
            