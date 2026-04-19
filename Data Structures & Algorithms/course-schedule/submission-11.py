class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for nodeA, nodeB in prerequisites:
            adj_list[nodeB].append(nodeA)
            indegree[nodeA] += 1

        queue = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        
        validCourses = 0

        while queue:
            currNode = queue.popleft()

            validCourses += 1

            for neighbor in adj_list[currNode]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
            
        return validCourses == numCourses
            