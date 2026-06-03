import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # [[5,2],[4,4],[4,1],[2,1],[3,3]]
        # sorted --> [[2,1],[3,3], [4,4],[4,1], [5,2]]
        # t = 2 + 1 [2, 1]
        # t = 3 + 3 [3, 3]
        # t = 6 + 4 [4, 1]
        # t = 10 + 5 [5, 2]
        # t = 15 + 4 [4, 4]

        tasks = [[t[0], t[1], i] for i, t in enumerate(tasks)]
        heapq.heapify(tasks)
        time = 0
        res = []

        while tasks:
            time += 1
            av_tasks = []
            while tasks and tasks[0][0] <= time:
                av_tasks.append(heapq.heappop(tasks))

            same_pr_tasks = []
            short_time = 0

            if av_tasks:
                av_tasks.sort(key = lambda x: x[1])
                short_time = av_tasks[0][1]
                for task in av_tasks:
                    if short_time == task[1]:
                        same_pr_tasks.append(task)
                    else:
                        heapq.heappush(tasks, task)

                selected_task = same_pr_tasks[0]
                if len(same_pr_tasks) > 1:
                    same_pr_tasks.sort(key = lambda x: x[2])
                    selected_task = same_pr_tasks[0]
                    for i in range(1, len(same_pr_tasks)):
                        heapq.heappush(tasks, same_pr_tasks[i])

                res.append(selected_task[2])
                time += selected_task[1] - 1 
                
        return res












