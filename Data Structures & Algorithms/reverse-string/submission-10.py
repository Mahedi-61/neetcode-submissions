class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # Python built-in function
        #s[:] = s[ : :-1]
        
        # O(1) memory
        # Two pointer approach
        # l = 0
        # r = len(s) - 1

        # while l < r:
        #     s[l], s[r] = s[r], s[l]
        #     l, r = l + 1, r - 1

        # using stack : not O(1)
        stack = s.copy()
        i = 0
        while stack:
            s[i] = stack.pop()
            i += 1