class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for sourceNode, destNode in prerequisites:
            adj_list[destNode].append(sourceNode)
            indegree[sourceNode] += 1

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
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = collections.defaultdict(list)

        for sourceNode, destNode in prerequisites:
            adj_list[destNode].append(sourceNode)
        
        visited = set()

        def dfs(currCourse):
            if currCourse in visited:
                return False
            
            if adj_list[currCourse] == []:
                return True
            
            visited.add(currCourse)
            for neighbor in adj_list[currCourse]:
                if not dfs(neighbor):
                    return False
            
            visited.remove(currCourse)

            # Mark all elements in the hash map list as visited
            adj_list[currCourse] = []

            return True
    
        for course in range (numCourses):
            if not dfs(course):
                return False
        
        return True
"""