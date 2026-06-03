class Solution:
    from collections import deque
    def openLock(self, deadends: List[str], target: str) -> int:
        # You have a lock with 4 circular wheels.
        # The lock initially starts at '0000'.
        # return the minimum total number of turns required to open the lock, 
        # or -1 if it is impossible.
        visit = set(deadends)
        q = deque(["0000"])
        count = 0
        if "0000" in visit:
            return -1

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node in visit: continue
                if node == target: return count
                visit.add(node)

                for i in range(len(node)):
                    h = int(node[i]) + 1
                    l = int(node[i]) - 1

                    if h == 10: h = 0
                    elif l == -1: l = 9

                    q.append(node[:i] + str(h) + node[i+1 : ])
                    q.append(node[:i] + str(l) + node[i+1 : ])

            count += 1
        return -1