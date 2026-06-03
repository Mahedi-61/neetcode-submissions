class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_dict = defaultdict(int)
        for i in range(len(order)):
            char_dict[order[i]] = i

        # can't solve 
        # try one by one word
        if len(words) < 2: return True 

        for i in range(1, len(words)):
            for j in range(0, len(words[i - 1])):
                if j >= len(words[i]) or char_dict[words[i - 1][j]] > char_dict[words[i][j]]:
                    return False

                elif char_dict[words[i - 1][j]] == char_dict[words[i][j]]:
                    continue
                else:
                    break

        return True  