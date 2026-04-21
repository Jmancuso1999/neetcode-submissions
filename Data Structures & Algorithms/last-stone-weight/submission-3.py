class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for index in range(len(stones)):
            stones[index] = -stones[index]

        heapq.heapify(stones)
        minHeap = stones

        while len(minHeap) >= 2:
            x = abs(heapq.heappop(minHeap))
            y = abs(heapq.heappop(minHeap))

            if x == y:
                continue
            else:
                heapq.heappush(minHeap, -abs(y - x))
        
        if len(minHeap) == 0:
            return 0
        
        return abs(minHeap[0])
"""
1. Brute Force 
     - Sort the array and append to a stack - O(n log n) time, space: O(n)
     - pick from the end 2 elements of the stack and reappend to the stack - O(n)

2. MaxHeap (Negative MinHeap) - O(n)
    - We store all the values as negatives and reappend to the heap
    - Continuously do this until the stack < 2

minHeap = heapq.heapify(stones) - store as negatives - [-1]


while len(minHeap) > 2:
    x = abs(first element popped from heap (heapq.heappop))
    y = abs(second element popped from heap)

    if x == y:
        continue
    else:
        heapq.heappush(minHeap, -abs(x - y))

if len(minHeap) == 1:
    return abs(minHeap[0])

return 0
"""