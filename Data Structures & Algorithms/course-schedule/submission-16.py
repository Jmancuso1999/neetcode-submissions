class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = collections.defaultdict(list)
        indegree = [0] * numCourses

        for course, preReq in prerequisites:
            adj_list[preReq].append(course)
            indegree[course] += 1
        
        queue = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        
        visited = set()

        while queue:
            currCourse = queue.popleft()

            if currCourse in visited:
                return False
            
            visited.add(currCourse)

            for neighborCourse in adj_list[currCourse]:
                indegree[neighborCourse] -= 1
                if indegree[neighborCourse] == 0:
                    queue.append(neighborCourse)
        
        for course in range(numCourses):
            if course not in visited:
                return False
        
        return True