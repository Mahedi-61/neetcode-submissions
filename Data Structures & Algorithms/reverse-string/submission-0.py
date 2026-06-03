class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        if len(s) < 2: return s 
        s[:] =  s[::-1]
        