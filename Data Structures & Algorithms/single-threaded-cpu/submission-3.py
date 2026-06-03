import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted([[et, pt, i] for i, (et, pt) in enumerate(tasks)]) 
        same_task = []
        time = 0
        res = []
        n = len(tasks)
        i = 0

        while i < n or same_task:
            while i < n and tasks[i][0] <= time:
                heapq.heappush(same_task, tasks[i][1:]) 
                i += 1

            if same_task:
                temp = heapq.heappop(same_task)
                time +=  temp[0]
                res.append(temp[1])
            else:
                # No task is available; fast-forward time
                time = tasks[i][0]
        return res
