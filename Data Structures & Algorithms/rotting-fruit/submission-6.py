class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()
        totalMinutes = 0
        freshCount = 0 # If fresh count is > 1 means we didnt convert all to rotten fruits
        ROWS, COLS = len(grid), len(grid[0])

        # Time: O(m * n)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    freshCount += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))
        
        # Time: O(m * n) - This reperesents the total # of mins, it would never be > m * n
        while queue and freshCount > 0:
            queueLen = len(queue)

            # At most O(queueLen)
            for _ in range(queueLen):
                currRotten = queue.popleft()
                # At most O(4)
                for x, y in directions:
                    directionX = currRotten[0] + x
                    directionY = currRotten[1] + y

                    if 0 <= directionX < ROWS and 0 <= directionY < COLS and grid[directionX][directionY] == 1:
                        grid[directionX][directionY] = 2
                        freshCount -= 1
                        queue.append((directionX, directionY))
            
            totalMinutes += 1

        # Didnt reach all the fresh fruit
        if freshCount > 0:
            return -1
        
        return totalMinutes