class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:

        j = len(s) - 1
        status = [False] * len(s)

        if s[j] == "1":
            return False
        else:
            status[j] = True

        while j >= 0:
            for i in range(minJump, maxJump + 1):
                if s[j - i] == "1" or status[j] == False:
                    continue
                else:
                    status[j-i] = True

            j -= 1
        print(status)
        return status[0] 