class Solution:
    def decodeString(self, s: str) -> str:
        num = 0
        chars = ""
        num_stack = []
        char_stack = []

        for c in s:
            if c.isdigit():
                num = (num * 10) + int(c)

            elif c == "[":
                char_stack.append(chars)
                num_stack.append(num)
                chars = ""
                num = 0

            elif c == "]":
                temp = chars * num_stack.pop()
                chars = char_stack.pop() + temp

            else:
                chars += c
        
        return chars
