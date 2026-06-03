class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        def bfs(q):
            def incr(temp):
                temp = int(temp) + 1
                if temp == 10: temp = 0
                return str(temp)

            def decr(temp):
                temp = int(temp) - 1
                if temp == -1: temp = 9
                return str(temp) 

            level = 0
            while q:
                for _ in range(len(q)):
                    states = q.popleft()
                    if states == target:
                        return level

                    first, second, third, four = states[0], states[1], states[2], states[3]
                    new_state = incr(first) + states[1:]
                    if new_state not in visit:
                        q.append(new_state)
                        visit.add(new_state)

                    new_state = decr(first) + states[1:]
                    if new_state not in visit:
                        q.append(new_state)
                        visit.add(new_state)

                    new_state = states[0] + incr(second) + states[2:]
                    if new_state not in visit:
                        q.append(new_state)
                        visit.add(new_state)

                    new_state = states[0] + decr(second) + states[2:]
                    if new_state not in visit:
                        q.append(new_state)
                        visit.add(new_state)

                    new_state = states[:2] + incr(third) + states[3]
                    if new_state not in visit:
                        q.append(new_state)
                        visit.add(new_state)

                    new_state = states[:2] + decr(third) + states[3]
                    if new_state not in visit:
                        q.append(new_state)
                        visit.add(new_state)

                    new_state = states[:3] + incr(four)
                    if new_state not in visit:
                        q.append(new_state)
                        visit.add(new_state)

                    new_state = states[:3] + decr(four)
                    if new_state not in visit:
                        q.append(new_state)
                        visit.add(new_state)

                level += 1
            return -1

        visit = set(deadends)
        q = deque(["0000"])
        if "0000" in visit:
            return -1
        elif "0000" == target:
            return 0
            
        return bfs(q)
        