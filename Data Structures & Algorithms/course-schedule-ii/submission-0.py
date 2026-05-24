from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = defaultdict(list)
        indegrees = defaultdict(int)
        for course, prereq in prerequisites:
            prereqs[prereq].append(course)
            indegrees[course] += 1
        queue = deque()
        queue.extend([i for i in range(numCourses) if indegrees[i] == 0])
        topological_sort = []
        while queue:
            course = queue.popleft()
            coursePrereqs = prereqs[course]
            topological_sort.append(course)
            for p in coursePrereqs:
                indegrees[p] -= 1
                if indegrees[p] == 0:
                    queue.append(p)
        is_dag = len([i for i in range(numCourses) if indegrees[i] == 0]) == numCourses
        return topological_sort if is_dag else []
