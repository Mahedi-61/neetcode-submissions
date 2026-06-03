class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dict_bill = {"5":0, "10":0, "20":0}

        for b in bills:
            if b == 5:
                dict_bill["5"] += 1

            elif b == 10:
                if dict_bill["5"] != 0:
                    dict_bill["5"] -= 1
                    dict_bill["10"] += 1
                else:
                    return False

            else:
                if dict_bill["10"] > 0 and dict_bill["5"] > 0:
                    dict_bill["10"] -= 1
                    dict_bill["5"] -= 1

                elif dict_bill["5"] >= 3:
                    dict_bill["5"] -= 3

                else:
                    return False

        return True