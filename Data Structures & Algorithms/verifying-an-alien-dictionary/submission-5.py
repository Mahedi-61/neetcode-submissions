class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_dict = {}
        for i, o in enumerate(order):
            char_dict[o] = i + 1
        
        #checking pairs of words
        for w1, w2 in zip(words, words[1:]):
            for i in range(len(w1)):
                if i == len(w2):
                    return False

                if w1[i] != w2[i]:
                    w1_char_idx = char_dict[w1[i]]
                    w2_char_idx = char_dict[w2[i]]

                    if w1_char_idx < w2_char_idx:
                        break
                    else:
                        return False

        return True 