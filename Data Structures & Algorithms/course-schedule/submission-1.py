class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        
        # Build adjacency list
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        def dfs(path, course):
            if course in path:
                return False  # cycle detected
            path.append(course)
            if course in graph:
                for prereq in graph[course]:
                    if not dfs(path, prereq):
                        return False
            path.pop()  # backtrack
            return True

        # Run DFS on each course
        for course in range(numCourses):
            if not dfs([], course):
                return False
        return True
                