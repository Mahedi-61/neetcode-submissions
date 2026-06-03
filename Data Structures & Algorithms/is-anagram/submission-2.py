class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # using python3 default function
        return sorted(s) == sorted(t)

        # using hash map 
        