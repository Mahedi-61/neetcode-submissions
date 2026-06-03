class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # finding cycle in directed graph
        # make dictionary
        hs_course = defaultdict(list)
        for pre in prerequisites:
            hs_course[pre[0]].append(pre[1])
        
        #DFS call
        def dfs(course):
            if len(hs_course[course]) == 0:
                return True

            if course in visit:
                return False

            visit.add(course)
            for pre in hs_course[course]:
                if dfs(pre):
                    continue
                else:
                    return False

            visit.remove(course)
            hs_course[pre] = []
            return True

        # iterate over all courses
        visit = set()
        for c in range(0, numCourses):
            if dfs(c):
                continue
            else:
                return False
        return True