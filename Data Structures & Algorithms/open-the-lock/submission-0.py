class Solution:
    from  collections import deque
    def openLock(self, deadends: List[str], target: str) -> int:
        # You have a lock with 4 circular wheels.
        # The lock initially starts at '0000', a string representing the state of the 4 wheels.
        # return the minimum total number of turns required to open the lock, 
        # or -1 if it is impossible.
        
        deadends = set(deadends)
        visit = set()
        q = deque(["0000"])
        count = 0

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node in visit: continue
                elif node in deadends: continue

                if node == target: return count
                visit.add(node)

                for i in range(len(node)):
                    temp = int(node[i])
                    h = temp + 1
                    l = temp - 1

                    if h == 10: h = 0
                    elif l == -1: l = 9

                    q.append(node[:i] + str(h) + node[i+1 : ])
                    q.append(node[:i] + str(l) + node[i+1 : ])
            count += 1
            
        return -1