class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        if len(s) < 2: return s 
        #s[:] =  s[::-1]

        #two pointer approach
        i = 0 
        j = len(s) - 1

        while i < len(s) // 2:
            s[i], s[j] = s[j], s[i]
            j -= 1
            i += 1