class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = {}

        for node in range(1, n + 1):
            adj_list[node] = []
        
        for sourceNode, destNode, weight in times:
            adj_list[sourceNode].append([destNode, weight])
        
        minHeap = [[0, k]] # Starting point
        visited = set()
        totalWeight = 0

        while minHeap:
            currWeight, currNode = heapq.heappop(minHeap)
        
            if currNode in visited:
                continue
            
            visited.add(currNode)

            # Total weight to visit all nodes
            totalWeight = currWeight

            for neighborNode, neighborWeight in adj_list[currNode]:
                heapq.heappush(minHeap, [currWeight + neighborWeight, neighborNode])
        
        # Need to check if all the nodes were visited, if not return -1
        for node in range(1, n + 1):
            if node not in visited:
                return -1
        
        return totalWeight