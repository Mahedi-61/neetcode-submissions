class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)

        def bfs(q, count):
            while q:
                seq, count = q.popleft()
                if seq == target:  return count
                if seq in visited: continue
                if seq in deadends: continue

                visited.add(seq)
                count += 1
                for idx in range(len(seq)):
                    d = int(seq[idx]) + 1
                    if d == 10: d = 0
                    q.append([seq[ : idx] + str(d) + seq[idx + 1 : ], count])

                for idx in range(len(seq)):
                    d = int(seq[idx]) - 1
                    if d == -1: d = 9
                    q.append([seq[ : idx] + str(d) + seq[idx + 1 : ], count])

            return -1


        q = collections.deque()
        q.append(["0000", 0])
        visited = set()
        count = bfs(q, count=1)
        print(visited)
        return count
