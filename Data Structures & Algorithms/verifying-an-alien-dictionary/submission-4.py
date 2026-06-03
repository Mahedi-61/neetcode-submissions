class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_dict = {"" : 0}
        for i, o in enumerate(order):
            char_dict[o] = i + 1
        
        i = 0 #position of chars
        while len(words) > 1:
           
            j = 0 #position of words
            while j < len(words) - 1:
                char1 = words[j][i] if i < len(words[j]) else ""
                char2 = words[j+1][i] if i < len(words[j+1]) else ""

                c_num1 = char_dict[char1]
                c_num2 = char_dict[char2]

                if c_num1 > c_num2:
                    return False
                elif c_num1 < c_num2:
                    del words[j]
                else:
                    j += 1

            i += 1

        return True