class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return res

        char_map = {"2": "abc", "3":"def", "4":"ghi",
                    "5": "jkl", "6":"mno", "7":"pqrs",
                    "8": "tuv", "9":"wxyz"}

        res = [c for c in char_map[digits[0]]]

        for i in range(1, len(digits)):
            temp = []
            for c in char_map[digits[i]]:
                for r in res:
                    temp.append(r + c)

            del res
            res = temp

        return res