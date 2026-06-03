class FreqStack:
    def __init__(self):
        self.stack = {}
        self.freq_stack = []
        self.time = 0

    def push(self, val: int) -> None:
        self.time += 1

        if val in self.stack:
            max_freq = self.stack[val]
            max_freq += 1
            self.stack[val] = max_freq

            if max_freq > len(self.freq_stack):
                self.freq_stack.append([(val, self.time)])
            else:
                self.freq_stack[max_freq-1].append((val, self.time))

        else:
            self.stack[val] = 1
            if len(self.freq_stack) == 0:
                self.freq_stack.append([(val, self.time)])
            else:
                self.freq_stack[0].append((val, self.time))


    def pop(self) -> int:
        v, t = self.freq_stack[-1][-1]
        freq = self.stack[v]

        if freq == 1:
            del self.stack[v]
        elif freq > 1:
            self.stack[v] -= 1

        if len(self.freq_stack[-1]) == 1:
            del self.freq_stack[-1]
        else:
            del self.freq_stack[-1][-1]

        return v


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()