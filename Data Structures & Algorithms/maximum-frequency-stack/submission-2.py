class FreqStack:
    def __init__(self):
        self.stack = []
        self.time = 0
        self.dt_val = defaultdict(int)

    def push(self, val: int) -> None:
        self.dt_val[val] += 1
        self.time += 1
        heapq.heappush(self.stack, [-self.dt_val[val], self.time, val])
        
    def pop(self) -> int:
        out = heapq.heappop(self.stack)
        ls = [out]
        while self.stack:
            temp = heapq.heappop(self.stack)
            if out[0] == temp[0]:
                ls.append(temp)
            else:
                heapq.heappush(self.stack, temp)
                break

        if len(ls) == 1:
            val = ls[0][2]
            self.dt_val[val] -= 1
            return val 

        else:
            t = max(l[1] for l in ls)
            for l in ls:
                if t == l[1]:
                    temp = l
                else:
                    heapq.heappush(self.stack, l)

            val = temp[2]
            self.dt_val[val] -= 1
            return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()