class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        total_time = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        
        # Keep count of all the fresh fruits so when we reach then end, we can verify if anymore remain
        fresh_count = 0

        queue = deque()

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    queue.append([row, col])
                elif grid[row][col] == 1:
                    fresh_count += 1
        
        while queue and fresh_count > 0:
            queue_len = len(queue)

            for _ in range(queue_len):
                currRow, currCol = queue.popleft() #[2,2]

                for dx, dy in directions:
                    newX = currRow + dx
                    newY = currCol + dy

                    if newX >= 0 and newX < ROWS and newY >= 0 and newY < COLS and grid[newX][newY] == 1:
                        fresh_count -= 1
                        grid[newX][newY] = 2
                        queue.append([newX, newY]) # Add to the queue to continue iterating
            
            total_time += 1

        if fresh_count != 0:
            return -1
        
        return total_time