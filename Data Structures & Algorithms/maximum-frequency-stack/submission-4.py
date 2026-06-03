class FreqStack:
    def __init__(self):
        self.max_freq = 0
        self.dt_count = defaultdict(int)
        self.dt_vals = defaultdict(list)

    def push(self, val: int) -> None:
        self.dt_count[val] += 1
        freq = self.dt_count[val]

        self.dt_vals[freq].append(val)
        if freq > self.max_freq:
            self.max_freq = freq
        
    def pop(self) -> int:
        val = self.dt_vals[self.max_freq].pop()
        self.dt_count[val] -= 1

        if self.dt_vals[self.max_freq] == []:
            self.max_freq -= 1

        return val