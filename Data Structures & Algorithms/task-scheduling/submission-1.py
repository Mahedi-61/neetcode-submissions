import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_dict = defaultdict(int)

        for t in tasks:
            task_dict[t] += 1

        heap = [-task_dict[t] for t in task_dict]
        heapq.heapify(heap)

        count = 0
        time = 0
        queue = []

        while heap or queue:
            time += 1
            count += 1
            if queue:
                if time > queue[0][1]:
                    heapq.heappush(heap, queue.pop(0)[0])
                else:
                    if len(heap) == 0: 
                        continue
            
            freq = heapq.heappop(heap)
            freq = abs(freq) - 1

            if freq == 0:
                pass 
            
            elif freq > 0 and n == 0:
                heapq.heappush(heap, -freq)

            else:
                queue.append((-freq, time + n))
        return count
                