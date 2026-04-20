class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dikstra's Algorithm way - Total time: O(VlogE+ElogE)≈O(ElogV)
        adj_list = collections.defaultdict(list)
        
        # O(E) - Times is literally all the Edges
        for source, destination, weight in times:
            adj_list[source].append([destination, weight])
        
        minHeap = [[0, k]] # k is the source
        visited = set()
        networkWeight = 0

        # O(V) - Total is O(V log E)
        while minHeap:
            weight, currNode = heapq.heappop(minHeap) # O(log V) (worse case)

            if currNode in visited:
                continue
            
            # Mark node as visited
            visited.add(currNode)

            # Increase network work
            networkWeight = weight

            # O(E) - Total is O(E log E)
            for neighbor, neighborWeight in adj_list[currNode]:
                if neighbor not in visited:
                                            # Computes total weight to visit all nodes
                    heapq.heappush(minHeap, [weight + neighborWeight, neighbor]) # O(log V)
            
        if len(visited) != n:
            return -1
        
        return networkWeight
        