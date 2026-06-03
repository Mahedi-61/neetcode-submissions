class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        saved_five = 0
        saved_ten = 0
        saved_twenty = 0

        for b in bills:
            if b == 5:
                saved_five += 1

            elif b == 10:
                if saved_five > 0:
                    saved_five -= 1
                    saved_ten += 1
                else:
                    return False 

            elif b == 20:
                if saved_ten > 0 and saved_five > 0:
                    saved_ten -= 1
                    saved_five -= 1
                    saved_twenty += 20
                
                elif saved_five > 2:
                    saved_five -= 3
                    saved_twenty += 20
                else:
                    return False 

        return True 
            
