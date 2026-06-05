class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dict_anag = defaultdict(list)
        for word in strs:
            key = [0] * 26

            for c in word:
                key[ord(c) - ord('a')] += 1
            
            dict_anag[tuple(key)].append(word)

        return list(dict_anag.values())