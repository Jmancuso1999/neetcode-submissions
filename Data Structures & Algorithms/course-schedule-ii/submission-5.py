class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {}
        indegree = [0] * numCourses
        queue = deque()

        for course in range(numCourses):
            adj_list[course] = []
        
        for course, preReq in prerequisites:
            adj_list[preReq].append(course)
            indegree[course] += 1
        
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        
        courseOrder = [] # Desired output
        validCourses = 0 # # of courses valid (0 indegree)

        while queue:
            currCourse = queue.popleft()

            courseOrder.append(currCourse)
            validCourses += 1

            for neighborCourse in adj_list[currCourse]:
                indegree[neighborCourse] -= 1
                if indegree[neighborCourse] == 0:
                    queue.append(neighborCourse)
            
        # Validate all the courses were visited
        if validCourses != numCourses:
            return []

        return courseOrder

"""
If its impossible for us to finish all the courses return an empty list.

Otherwise return the ORDER of courses we need to do to complete all the courses.

Question:
1. What prevents us from finishing a course list? Cycle


To find a cycle in a directed acylic graph (DAG) we can do:
1. DFS
2. Khans Algorithm (Topoligcal Sort)

"""