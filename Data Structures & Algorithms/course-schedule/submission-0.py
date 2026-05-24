from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create adjacency list to represent prereq graph
        prereqs = defaultdict(list)
        # track the in-degree per course
        indegree = defaultdict(int)
        for course, prereq in prerequisites:
            prereqs[prereq].append(course)
            indegree[course] += 1
        queue = deque()
        queue.extend([i for i in range(numCourses) if indegree[i] == 0])
        while queue:
            course = queue.popleft()
            coursePrereqs = prereqs[course]
            for p in coursePrereqs:
                indegree[p] -= 1
                if indegree[p] == 0:
                    queue.append(p)
        return len([i for i in range(numCourses) if indegree[i] == 0]) == numCourses

        