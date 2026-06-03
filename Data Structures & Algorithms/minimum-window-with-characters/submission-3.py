class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #1. handle target substring 
        dict_t = defaultdict(int)
        for c in t:
            dict_t[c] += 1

        #2. handle given substring with indices list
        dict_s = defaultdict(deque)
        for i, c in enumerate(s):
            dict_s[c].append(i)

        # find the match
        ls_indices = set()
        for key, val in dict_t.items():
            if len(dict_s[key]) < val:
                return ""


            for _ in range(val):
                ls_indices.add(dict_s[key].popleft())
        
        # handle edge cases
        min_idx, max_idx = min(ls_indices), max(ls_indices)
        min_sub = s[min_idx : max_idx + 1]
        i = len(s) - 1


        if min_idx == max_idx: return s[min_idx]
        #elif i == max_idx: return min_sub
        
        # scan throught the list for min substring

        j = min_idx
        while j < len(s):
            if j in ls_indices:
                ls_indices.discard(j)
                key = s[j] 
                if len(dict_s[key]) == 0:
                    return min_sub
                
                new_idx = dict_s[key].popleft()
                ls_indices.add(new_idx)

                if new_idx > max_idx:
                    max_idx = new_idx
            j += 1
            text = s[j : max_idx + 1]
            if len(text) < len(min_sub):
                min_sub = text

        return min_sub





