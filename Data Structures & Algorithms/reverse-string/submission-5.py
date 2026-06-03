class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #s[:] =  s[::-1]

        # #two pointer approach
        # i = 0 
        # j = len(s) - 1

        # while i < j:
        #     s[i], s[j] = s[j], s[i]
        #     j -= 1
        #     i += 1

        #stack approach
        stack = s.copy()
        for i in range(len(s)):
            s[i] = stack.pop()