class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g_ag = {}

        for word in strs:
            sort_word = "".join(sorted(word))
            if sort_word in g_ag:
                g_ag[sort_word].append(word)

            else:
                g_ag[sort_word] = [word]

        return list(g_ag.values())