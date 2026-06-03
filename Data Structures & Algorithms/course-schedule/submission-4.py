class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # take dict
        courseMap = defaultdict(list)
        for pre in prerequisites:
            courseMap[pre[0]].append(pre[1])

        # DFS algorithm
        def dfs(course):
            if course in visit:
                return False
            if courseMap[course] == []:
                return True

            visit.add(course)
            for pre in courseMap[course]:
                if dfs(pre):
                    continue
                else:
                    return False

            visit.remove(course)
            courseMap[course] = []
            return True

        # iterate through
        visit = set()
        for cor in range(numCourses):
            if dfs(cor):
                continue
            else:
                return False

        return True 