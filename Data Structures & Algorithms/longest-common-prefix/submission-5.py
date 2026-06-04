class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #verticle scanning

        for i, c in enumerate(strs[0]):
            for word in strs[1:]:
                if i >= len(word) or c != word[i]:
                    return strs[0][:i]

        return strs[0]
